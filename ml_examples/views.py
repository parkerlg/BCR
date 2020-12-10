import json
import numpy as np
from urllib import request as r
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from .forms import dreamJobForm

# Create your views here.

def dreamJobView(request):
    if request.method == 'POST':
        form = dreamJobForm(request.POST)
        if form.is_valid():
            inputID = request.POST['job_title']
            try:

                data =  {
                            "Inputs": {
                                    "input1":
                                    {
                                        "ColumnNames": ["job_title"],
                                        "Values": [[
                            inputID,
                            ]]
                                    },
                            },
                        }
                body = str.encode(json.dumps(data))
                url = 'https://ussouthcentral.services.azureml.net/workspaces/e52f975d4320488386b8c05bc82f2238/services/0584b765f93b40b8844598279faf5ee8/execute?api-version=2.0&details=true'
                api_key = 'H9hsb8o+KykvXyeD6QvqUiMO44tx8kBR2wunZBGr1nSSu0pFESUjM5k+FtXtDARaedqjEnakmAnCnOj1t+qy6g==' # Replace this with the API key for the web service
                headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}
                #Generate web service request
                req =r.Request(url, body, headers)
                req.method = "POST"
                response = r.urlopen(req)
                result = response.read()
                result = json.loads(result)
                prediction = result['Results']['output1']['value']['Values'][0]

                data = {'matchbox_results':str(f'1. {prediction[0]}, 2.{prediction[1]}, 3.{prediction[2]},4.{prediction[3]},5.{prediction[4]}')}

                context = {
                    'form' : form,
                    'check': True,
                    'value1': prediction[0],
                    'value2': prediction[1],
                    'value3': prediction[2],
                    'value4': prediction[3],
                    'value5': prediction[4]

                }
                return render(request, 'User/dream_job.html', context)
            except:
                context = {
                    'check': False,
                    'message' : 'Please enter a correct value'
                }
            return render(request, 'User/dream_job.html', context)

    # if a GET (or any other method) we'll create a blank form
    
    form = dreamJobForm()

    return render(request, 'User/dream_job.html', {'form': form})
#  # Convert JSON byte stream into dictionary
#     # try:
#     form = dreamJobForm()
#         # data =  {
#         #         "Inputs": {
#         #                 "input1":
#         #                 {
#         #                     "ColumnNames": ["job_title"],
#         #                     "Values": [[
#         #         request.GET['inputID'],
#         #         ]]
#         #                 },
#         #         },
#         #     }
#         # body = str.encode(json.dumps(data))
#         # url = 'https://ussouthcentral.services.azureml.net/workspaces/e52f975d4320488386b8c05bc82f2238/services/0584b765f93b40b8844598279faf5ee8/execute?api-version=2.0&details=true'
#         # api_key = 'H9hsb8o+KykvXyeD6QvqUiMO44tx8kBR2wunZBGr1nSSu0pFESUjM5k+FtXtDARaedqjEnakmAnCnOj1t+qy6g==' # Replace this with the API key for the web service
#         # headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}
#         # #Generate web service request
#         # req =r.Request(url, body, headers)
#         # req.method = "POST"
#         # response = r.urlopen(req)
#         # result = response.read()
#         # result = json.loads(result)
#         # prediction = result['Results']['output1']['value']['Values'][0]

#         # data = {'matchbox_results':str(f'1. {prediction[0]}, 2.{prediction[1]}, 3.{prediction[2]},4.{prediction[3]},5.{prediction[4]}')}
#     context = {
#         'form' : form,
#             # 'check': True,
#             # 'value1': prediction[0],
#             # 'value2': prediction[1],
#             # 'value3': prediction[2],
#             # 'value4': prediction[3],
#             # 'value5': prediction[4]

#     }
#     return render(request, 'User/dream_job.html', context)
#     # except:
#     #     context = {
#     #         'check': False,
#     #         'message' : 'Please enter a correct value'
#     #     }
#         # return render(request, 'User/dream_job.html', context)