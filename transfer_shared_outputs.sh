#!/bin/bash

mkdir /compute_shared/${job_id}

cd ${result_folder}

cp *.tiff /compute_shared/${job_id}/
