import os
from glob import glob
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from netCDF4 import Dataset
import csv
from lib.map import get_countries_mask, get_grid_area, get_pop
from lib.helper import pop_ssp_dict


pm25_path = "/project/ccr02/lamar/CMIP6_analysis/PM2.5/annual_0.5x0.5"
mort_path = "/project/ccr02/lamar/CMIP6_analysis/PM2.5/Health"
ssps = ["ssp126", "ssp245", "ssp370", "ssp585"]


def mean(ssp, year, fractionCountries, type):
    """Compute the mean PM2.5 concentration, given SSP, year, and countries fractions"""
    if type not in ["PM2.5 Concentration", "Mortality"]:
        raise Exception(f"Unknown type {type}")
    grid_area, tot_area = get_grid_area(fractionCountries)
    pop, tot_pop = get_pop(ssp, year, fractionCountries)
    pop_ssp = pop_ssp_dict[ssp]

    all_data = []  # Unweighted mean
    all_awm = []  # Area weighted mean
    all_pwm = []  # Population weighted mean
    models = os.listdir(os.path.join(pm25_path, ssp, "mmrpm2p5"))

    for model in models:
        # Outlier: extremely large data
        if "EC-Earth3" in model:
            continue
        if "IPSL" in model or "MPI" in model:
            continue
        # Skip models that do not include natural PM2.5 sources (anthropogenic only)
        # if model not in ["GFDL-ESM4", "MRI-ESM2-0"]:
        #     continue

        # Compute mean PM2.5 concentration of all realizations
        if type == "PM2.5 Concentration":
            search_str = os.path.join(
                pm25_path, ssp, "mmrpm2p5", model, "*", f"annual_avg_{year}.nc"
            )
            files = sorted(glob(search_str))
        elif type == "Mortality":
            search_str = os.path.join(
                mort_path,
                "Baseline_Ben_2040_National",
                "5_years",
                ssp,
                f"Pop_{pop_ssp}_var",
                "MortalityAbsolute",
                "Allcause_mean",
                f"{model}_*_{year}_GEMM.nc",
            )
            files = sorted(glob(search_str))
        if len(files) == 0:
            raise Exception(f"{search_str} not found!")
        model_data = []
        model_awm = []
        model_pwm = []

        for file in files:
            # Import concentration NC file
            wk = Dataset(file, "r")
            if type == "PM2.5 Concentration":
                data = wk["concpm2p5"][:]
                country_data = (
                    data * fractionCountries * (10**9)
                )  # Apply mask to concentration array
            elif type == "Mortality":
                data = wk["deaths__mean"]
                country_data = data * fractionCountries

            area_weighted_mean = np.sum(grid_area * country_data) / tot_area
            pop_weighted_mean = np.sum(pop * country_data) / tot_pop

            # Compute mean concentration of every province
            # state_means = np.zeros(len(states))
            # for k, state in enumerate(states):
            #     state_conc = conc * fractionState[k] * (10 ** 9)
            #     state_area = np.sum(fractionState[k])
            #     state_means[k] = np.sum(state_conc) / state_area
            # all_conc.append(state_means)

            model_data.append(country_data)
            model_awm.append(area_weighted_mean)
            model_pwm.append(pop_weighted_mean)

        model_data = np.mean(model_data, axis=0)
        model_awm = np.mean(model_awm, axis=0)
        model_pwm = np.mean(model_pwm, axis=0)
        all_data.append(model_data)
        all_awm.append(model_awm)
        all_pwm.append(model_pwm)
        # print(f"{model}: PWM: {np.round(model_pwm, 2)}, AWM: {np.round(model_awm, 2)}")

    all_data = np.mean(all_data, axis=0)
    all_awm = np.mean(all_awm, axis=0)
    all_pwm = np.mean(all_pwm, axis=0)
    return all_data, all_awm, all_pwm


def get_means(regions, region_countries, region_countries_names, ssp, year, type):
    """Return mean values of input regions"""
    awms = np.zeros(len(regions))
    pwms = np.zeros(len(regions))
    for i, (region, countries, countries_names) in enumerate(
        zip(regions, region_countries, region_countries_names)
    ):
        # Get country mask
        fractionCountries = get_countries_mask(countries=countries)

        # Get grid areas for area weighted mean
        grid_area, tot_area = get_grid_area(fractionCountries)

        # Get population for population weighted mean
        pop, tot_pop = get_pop(ssp, year, fractionCountries)
        conc, awm, pwm = mean(ssp, year, fractionCountries, type)
        # print(f"{ssp} Region {region} has AWM {awm}, PWM {pwm}")
        awms[i] = awm
        pwms[i] = pwm
    return awms, pwms


def output_means(regions, region_countries, region_countries_names):
    awms = []
    pwms = []
    for ssp in ssps:
        awm, pwm = get_means(
            regions,
            region_countries,
            region_countries_names,
            ssp=ssp,
            year=2015,
            type="Concentration",
        )
        awms.append(awm)
        pwms.append(pwm)
    awms = np.mean(awms, axis=0)
    pwms = np.mean(pwms, axis=0)

    output_dir = "/home/ybenp/CMIP6_Images/PM2.5/map"
    output_file = os.path.join(output_dir, "2015_mean.csv")
    with open(output_file, "w") as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(["Region Name", "AWM", "PWM"])
        for i, region in enumerate(regions):
            csvwriter.writerow([region, awms[i], pwms[i]])
            print(f"Region {region}: has AWM {awms[i]} and PWM {pwms[i]}")
