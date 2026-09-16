#!/bin/bash

input_file=$1
output_file="converted_$input_file"

tr ';' ',' < "$input_file" > "$output_file"