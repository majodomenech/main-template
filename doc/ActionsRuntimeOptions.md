# ActionsRuntimeOptions

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **AllOfActionsRuntimeOptionsType** |  | 
**date_range** | **OneOfActionsRuntimeOptionsDateRange** | This property specifies the date range across which the request will search for corporate actions. Any &#x60;ActionsRequest&#x60; that references a recurring &#x60;ScheduledTrigger&#x60; (where the frequency is \&quot;daily\&quot; \&quot;weekday\&quot; \&quot;weekend\&quot; \&quot;weekly\&quot; or \&quot;monthly\&quot;) may only specify a &#x60;ActionsDurationDateRange&#x60;, ensuring the date range remains relative to each execution of the request. An &#x60;ActionsRequest&#x60; that references a trigger which will only execute once (a &#x60;ScheduledTrigger&#x60; with a frequency of \&quot;once\&quot; or a &#x60;SubmitTrigger&#x60;) can also specify a date range using literal dates using an &#x60;IntervalDateRange&#x60;. If this property is not supplied, the range will default to an &#x60;ActionsDurationDateRange&#x60; with 0 &#x60;days&#x60;. | [optional] 
**actions_date** | **str** | Apply the specified dateRange to the date the action was recorded by Bloomberg (&#x60;entry&#x60;), the date as of which the action is effective (&#x60;effective&#x60;) or either (&#x60;both&#x60;). | [optional] [default to 'entry']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

