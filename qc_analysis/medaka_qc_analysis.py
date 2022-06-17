#!/usr/bin/env python
# coding: utf-8
############################################################################################################
# Authors:
#   Anirudh Bhashyam, Uni Heidelberg, anirudh.bhashyam@stud.uni-heidelberg.de   (Current Maintainer)
# Date: 04/2022
# License: Contact authors
###
# Algorithms for:
#   Decision tree evaluation by medaka_bpm.
###
############################################################################################################
import os
import sys
import argparse

import decision_tree.src.analysis as analyse

def process_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input_file", help = "Results from medaka_bpm", type = str, required = True)
    parser.add_argument("-o", "--out_dir",  help = "Directory to write analysis results", type = str, required = True)
    return parser.parse_args()

def main():
    args = process_args()
    raw_data = analyse.pd.read_csv(args.input_file)
    data, scale = analyse.process_data(raw_data, 20)
    classifier, classifier_results = analyse.decision_tree(data)
    limits = analyse.get_thresholds(raw_data, analyse.QC_FEATURES, classifier)
    analyse.write_results(raw_data, data, classifier, classifier_results, limits, args.out_dir)
    
if __name__ == "__main__":
    main()