#!/bin/bash

echo -e "Compute standard deviation\n"

echo -e "confused\n"
python computeStandardDeviations.py confused_large_filter_difference_with_real_value.txt standard_deviations/confused_large_filter_difference_with_real_value.txt
python computeStandardDeviations.py confused_large_filter_pacman_belief_state_summary.txt standard_deviations/confused_large_filter_pacman_belief_state_summary.txt
python computeStandardDeviations.py confused_large_filter_walls_difference_with_real_value.txt standard_deviations/confused_large_filter_walls_difference_with_real_value.txt
python computeStandardDeviations.py confused_large_filter_walls_pacman_belief_state_summary.txt standard_deviations/confused_large_filter_walls_pacman_belief_state_summary.txt

echo -e "afraid\n"
python computeStandardDeviations.py afraid_large_filter_difference_with_real_value.txt standard_deviations/afraid_large_filter_difference_with_real_value.txt
python computeStandardDeviations.py afraid_large_filter_pacman_belief_state_summary.txt standard_deviations/afraid_large_filter_pacman_belief_state_summary.txt
python computeStandardDeviations.py afraid_large_filter_walls_difference_with_real_value.txt standard_deviations/afraid_large_filter_walls_difference_with_real_value.txt
python computeStandardDeviations.py afraid_large_filter_walls_pacman_belief_state_summary.txt standard_deviations/afraid_large_filter_walls_pacman_belief_state_summary.txt

echo -e "scared\n"
python computeStandardDeviations.py scared_large_filter_difference_with_real_value.txt standard_deviations/scared_large_filter_difference_with_real_value.txt
python computeStandardDeviations.py scared_large_filter_pacman_belief_state_summary.txt standard_deviations/scared_large_filter_pacman_belief_state_summary.txt
python computeStandardDeviations.py scared_large_filter_walls_difference_with_real_value.txt standard_deviations/scared_large_filter_walls_difference_with_real_value.txt
python computeStandardDeviations.py scared_large_filter_walls_pacman_belief_state_summary.txt standard_deviations/scared_large_filter_walls_pacman_belief_state_summary.txt