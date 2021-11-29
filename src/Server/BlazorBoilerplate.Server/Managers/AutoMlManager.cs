﻿using BlazorBoilerplate.Infrastructure.Server;
using BlazorBoilerplate.Infrastructure.Server.Models;
using BlazorBoilerplate.Shared.Dto.AutoML;
using BlazorBoilerplate.Storage;
using Newtonsoft.Json;
using Newtonsoft.Json.Linq;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using static Microsoft.AspNetCore.Http.StatusCodes;
using Google.Protobuf; 

namespace BlazorBoilerplate.Server.Managers
{
    /// <summary>
    /// Manages all RPC calls related to AutoMl process
    /// </summary>
    public class AutoMlManager : IAutoMlManager
    {
        private readonly ApplicationDbContext _dbContext;
        private readonly ControllerService.ControllerServiceClient _client;
        public AutoMlManager(ApplicationDbContext dbContext, ControllerService.ControllerServiceClient client)
        {
            _dbContext = dbContext;
            _client = client;
        }
        /// <summary>
        /// Get the result model from a specific AutoML
        /// </summary>
        /// <param name="autoMl"></param>
        /// <returns></returns>
        public async Task<ApiResponse> GetModel(GetAutoMlModelRequestDto autoMl)
        {
            GetAutoMlModelRespomseDto response = new GetAutoMlModelRespomseDto();
            GetAutoMlModelRequest getmodelRequest = new GetAutoMlModelRequest();
            try
            {
                getmodelRequest.SessionId = autoMl.SessionId;
                getmodelRequest.AutoMl = autoMl.AutoMl;
                var reply = _client.GetAutoMlModel(getmodelRequest);
                response.Name = reply.Name;
                response.Content = reply.File.ToByteArray();
                return new ApiResponse(Status200OK, null, response);

            }
            catch (Exception ex)
            {

                return new ApiResponse(Status404NotFound, ex.Message);
            }
        }
        /// <summary>
        /// Start the OMAML process to search for a model
        /// </summary>
        /// <param name="autoMl"></param>
        /// <returns></returns>
        public async Task<ApiResponse> Start(StartAutoMLRequestDto autoMl)
        {
            StartAutoMLResponseDto response = new StartAutoMLResponseDto();
            StartAutoMLprocessRequest startAutoMLrequest = new StartAutoMLprocessRequest();
            try
            {
                startAutoMLrequest.Dataset = autoMl.DatasetName;
                startAutoMLrequest.Task = GetMachineLearningTask(autoMl);
                startAutoMLrequest.TabularConfig = GetTabularDataConfiguration(autoMl);
                // TODO consider to refactor
                startAutoMLrequest.RuntimeConstraints = new AutoMLRuntimeConstraints
                {
                    MaxIter = autoMl.RuntimeConstraints.Max_iter,
                    RuntimeLimit = autoMl.RuntimeConstraints.Runtime_limit
                };
                var reply = _client.StartAutoMLprocess(startAutoMLrequest);
                if (reply.Result == ControllerReturnCode.Success)
                {
                    response.SessionId = reply.SessionId;
                    return new ApiResponse(Status200OK, null, response);
                }
                else
                {
                    return new ApiResponse(Status400BadRequest, "Error while starting AutoML Code: " + reply.Result + "", null);
                }

            }
            catch (Exception ex)
            {

                return new ApiResponse(Status404NotFound, ex.Message);
            }
        }
        /// <summary>
        /// Convert AutoML task to enum equivalent
        /// </summary>
        /// <param name="autoMl"></param>
        /// <returns></returns>
        private MachineLearningTask GetMachineLearningTask(StartAutoMLRequestDto autoMl)
        {
            switch (autoMl.DatasetType)
            {
                case "TABULAR":
                    switch (autoMl.Task)
                    {
                        case "classification":
                            return MachineLearningTask.TabularClassification;
                        case "regression":
                            return MachineLearningTask.TabularRegression;
                        default:
                            return MachineLearningTask.Unknown;
                    }
                default:
                    return MachineLearningTask.Unknown;
            }
        }
        /// <summary>
        /// retrive the Tabular data configuration accordingly to correct template
        /// Needed since a correct conversion requires explicit knowledge of the JSON structure
        /// </summary>
        /// <param name="autoMl"></param>
        /// <returns></returns>
        private AutoMLConfigurationTabularData GetTabularDataConfiguration(StartAutoMLRequestDto autoMl)
        {
            switch (autoMl.DatasetType)
            {
                case "TABULAR":
                    AutoMLConfigurationTabularData conf = new AutoMLConfigurationTabularData();
                    conf.Target = new AutoMLTarget();
                    autoMl.Configuration = ((JObject)autoMl.Configuration).ToObject<AutoMLTabularDataConfiguration>();
                    conf.Target.Target = ((AutoMLTabularDataConfiguration)autoMl.Configuration).Target.Target;
                    conf.Target.Type = ((AutoMLTabularDataConfiguration)autoMl.Configuration).Target.Type;
                    return conf;
                default:
                    return null;
            }
        }
    }
}
