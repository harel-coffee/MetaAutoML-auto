﻿using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace BlazorBoilerplate.Shared.Dto.Model
{
    public class GetModelsRequestDto
    {
        public string DatasetIdentifier { get; set; }
        public bool Top3Only { get; set; }
    }
}
