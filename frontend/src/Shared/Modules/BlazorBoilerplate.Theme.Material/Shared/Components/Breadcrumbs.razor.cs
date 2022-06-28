﻿using BlazorBoilerplate.Shared.Localizer;
using Microsoft.AspNetCore.Components;
using Microsoft.Extensions.Localization;
using System.Collections.Generic;

namespace BlazorBoilerplate.Theme.Material.Shared.Components
{
    public partial class Breadcrumbs : ComponentBase
    {
        [Parameter]
        public RenderFragment ChildContent { get; set; }

        [Parameter]
        public bool IncludeRoot { get; set; } = true;

        protected internal List<Breadcrumb> Items = new();

        [Inject] protected IStringLocalizer<Global> L { get; set; }

        protected override void OnInitialized()
        {
            if (IncludeRoot)
                //Items.Insert(0, new Breadcrumb("/", L["BreadCrumbHome"]));
                Items.Insert(0, new Breadcrumb("/", "HOME"));
        }
    }
}
