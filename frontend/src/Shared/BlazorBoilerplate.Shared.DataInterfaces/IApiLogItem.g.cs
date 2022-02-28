//Autogenerated by BlazorBoilerplate.EntityGenerator
using BlazorBoilerplate.Constants;
using System;
using System.Collections.Generic;
using System.ComponentModel;

namespace BlazorBoilerplate.Shared.DataInterfaces
{
    public interface IApiLogItem
    {
        Int64 Id { get; set; }

        DateTime RequestTime { get; set; }

        Int64 ResponseMillis { get; set; }

        Int32 StatusCode { get; set; }

        String Method { get; set; }

        String Path { get; set; }

        String QueryString { get; set; }

        String RequestBody { get; set; }

        String ResponseBody { get; set; }

        String IPAddress { get; set; }

        Guid? ApplicationUserId { get; set; }

        IApplicationUser ApplicationUser { get; set; }

    }
}
