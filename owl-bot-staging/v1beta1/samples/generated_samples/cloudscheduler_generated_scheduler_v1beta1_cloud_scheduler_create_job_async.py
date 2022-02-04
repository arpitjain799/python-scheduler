# -*- coding: utf-8 -*-
# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Generated code. DO NOT EDIT!
#
# Snippet for CreateJob
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-scheduler


# [START cloudscheduler_generated_scheduler_v1beta1_CloudScheduler_CreateJob_async]
from google.cloud import scheduler_v1beta1


async def sample_create_job():
    # Create a client
    client = scheduler_v1beta1.CloudSchedulerAsyncClient()

    # Initialize request argument(s)
    request = scheduler_v1beta1.CreateJobRequest(
        parent="parent_value",
    )

    # Make the request
    response = await client.create_job(request=request)

    # Handle response
    print(response)

# [END cloudscheduler_generated_scheduler_v1beta1_CloudScheduler_CreateJob_async]
