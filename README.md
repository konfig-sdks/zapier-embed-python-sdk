<div align="center">

[![Visit Zapier](./header.png)](https://zapier.com)

# Zapier<a id="zapier"></a>

The Zapier Embed API.


</div>

## Table of Contents<a id="table-of-contents"></a>

<!-- toc -->

- [Requirements](#requirements)
- [Installation](#installation)
- [Getting Started](#getting-started)
- [Async](#async)
- [Raw HTTP Response](#raw-http-response)
- [Reference](#reference)
  * [`zapierembed.actions.get_choices`](#zapierembedactionsget_choices)
  * [`zapierembed.actions.get_input_fields`](#zapierembedactionsget_input_fields)
  * [`zapierembed.actions.get_output_fields`](#zapierembedactionsget_output_fields)
  * [`zapierembed.actions.list_available_actions`](#zapierembedactionslist_available_actions)
  * [`zapierembed.actions.test_action_execution`](#zapierembedactionstest_action_execution)
  * [`zapierembed.apps.list_popular`](#zapierembedappslist_popular)
  * [`zapierembed.authentications.create_new_authentication`](#zapierembedauthenticationscreate_new_authentication)
  * [`zapierembed.authentications.get_available`](#zapierembedauthenticationsget_available)
  * [`zapierembed.experimental.get_zap_runs`](#zapierembedexperimentalget_zap_runs)
  * [`zapierembed.zaps.create_zap`](#zapierembedzapscreate_zap)
  * [`zapierembed.zaps.get_filtered_zaps`](#zapierembedzapsget_filtered_zaps)

<!-- tocstop -->

## Requirements<a id="requirements"></a>

Python >=3.7

## Installation<a id="installation"></a>
<div align="center">
  <a href="https://konfigthis.com/sdk-sign-up?company=Zapier&serviceName=Embed&language=Python">
    <img src="https://raw.githubusercontent.com/konfig-dev/brand-assets/HEAD/cta-images/python-cta.png" width="70%">
  </a>
</div>

## Getting Started<a id="getting-started"></a>

```python
from pprint import pprint
from zapier_embed_python_sdk import ZapierEmbed, ApiException

zapierembed = ZapierEmbed()

try:
    # Get Choices
    get_choices_response = zapierembed.actions.get_choices(
        data={
            "authentication": "J2PlD7Rt",
        },
        action="uag:87b1c14e-ef30-43d5-9395-6c6514dbb123",
        input="lead_id",
        page="1",
    )
    print(get_choices_response)
except ApiException as e:
    print("Exception when calling ActionsApi.get_choices: %s\n" % e)
    pprint(e.body)
    if e.status == 404:
        pprint(e.body["errors"])
    if e.status == 415:
        pprint(e.body["errors"])
    if e.status == 406:
        pprint(e.body["errors"])
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```

## Async<a id="async"></a>

`async` support is available by prepending `a` to any method.

```python
import asyncio
from pprint import pprint
from zapier_embed_python_sdk import ZapierEmbed, ApiException

zapierembed = ZapierEmbed()


async def main():
    try:
        # Get Choices
        get_choices_response = await zapierembed.actions.aget_choices(
            data={
                "authentication": "J2PlD7Rt",
            },
            action="uag:87b1c14e-ef30-43d5-9395-6c6514dbb123",
            input="lead_id",
            page="1",
        )
        print(get_choices_response)
    except ApiException as e:
        print("Exception when calling ActionsApi.get_choices: %s\n" % e)
        pprint(e.body)
        if e.status == 404:
            pprint(e.body["errors"])
        if e.status == 415:
            pprint(e.body["errors"])
        if e.status == 406:
            pprint(e.body["errors"])
        pprint(e.headers)
        pprint(e.status)
        pprint(e.reason)
        pprint(e.round_trip_time)


asyncio.run(main())
```

## Raw HTTP Response<a id="raw-http-response"></a>

To access raw HTTP response values, use the `.raw` namespace.

```python
from pprint import pprint
from zapier_embed_python_sdk import ZapierEmbed, ApiException

zapierembed = ZapierEmbed()

try:
    # Get Choices
    get_choices_response = zapierembed.actions.raw.get_choices(
        data={
            "authentication": "J2PlD7Rt",
        },
        action="uag:87b1c14e-ef30-43d5-9395-6c6514dbb123",
        input="lead_id",
        page="1",
    )
    pprint(get_choices_response.body)
    pprint(get_choices_response.body["data"])
    pprint(get_choices_response.body["meta"])
    pprint(get_choices_response.body["links"])
    pprint(get_choices_response.headers)
    pprint(get_choices_response.status)
    pprint(get_choices_response.round_trip_time)
except ApiException as e:
    print("Exception when calling ActionsApi.get_choices: %s\n" % e)
    pprint(e.body)
    if e.status == 404:
        pprint(e.body["errors"])
    if e.status == 415:
        pprint(e.body["errors"])
    if e.status == 406:
        pprint(e.body["errors"])
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```


## Reference<a id="reference"></a>
### `zapierembed.actions.get_choices`<a id="zapierembedactionsget_choices"></a>

Get the possible values for an Input Field that is marked as `SELECT`.

This endpoint requires the `zap` OAuth scope.

This API is rate limited by IP address (60 requests per min), or partner (150 requests per min), whichever occurs first.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_choices_response = zapierembed.actions.get_choices(
    data={
        "authentication": "J2PlD7Rt",
    },
    action="uag:87b1c14e-ef30-43d5-9395-6c6514dbb123",
    input="lead_id",
    page="1",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### data: [`ActionsGetChoicesRequestData`](./zapier_embed_python_sdk/type/actions_get_choices_request_data.py)<a id="data-actionsgetchoicesrequestdatazapier_embed_python_sdktypeactions_get_choices_request_datapy"></a>


##### action: `str`<a id="action-str"></a>

An Action ID, as provided by the `/actions` endpoint.

##### input: `str`<a id="input-str"></a>

An Input Field ID, as provided by the `/inputs` endpoint.

##### page: `str`<a id="page-str"></a>

The page of choices to return, defaults to the first

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ActionsGetChoicesRequest`](./zapier_embed_python_sdk/type/actions_get_choices_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ActionsGetChoicesResponse`](./zapier_embed_python_sdk/pydantic/actions_get_choices_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/actions/{action}/inputs/{input}/choices` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `zapierembed.actions.get_input_fields`<a id="zapierembedactionsget_input_fields"></a>

Get the Input Fields for a particular Action, using the provided authentication and inputs.

This endpoint requires the `zap:write` OAuth scope.

This API is rate limited by IP address (60 requests per min), or partner (150 requests per min), whichever occurs first.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_input_fields_response = zapierembed.actions.get_input_fields(
    action="uag:87b1c14e-ef30-43d5-9395-6c6514dbb123",
    data={
        "authentication": None,
        "inputs": {},
    },
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### action: `str`<a id="action-str"></a>

An Action ID, as provided by the `/actions` endpoint.

##### data: [`InputsWithAuthenticationId`](./zapier_embed_python_sdk/type/inputs_with_authentication_id.py)<a id="data-inputswithauthenticationidzapier_embed_python_sdktypeinputs_with_authentication_idpy"></a>


#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ActionsGetInputFieldsRequest`](./zapier_embed_python_sdk/type/actions_get_input_fields_request.py)
Common inputs with inputs and an authentication id.

#### 🔄 Return<a id="🔄-return"></a>

[`ActionsGetInputFieldsResponse`](./zapier_embed_python_sdk/pydantic/actions_get_input_fields_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/actions/{action}/inputs` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `zapierembed.actions.get_output_fields`<a id="zapierembedactionsget_output_fields"></a>

Get the Output Fields for a particular Action, using the provided authentication and inputs.

This endpoint requires the `zap:write` OAuth scope.

This API is rate limited by IP address (60 requests per min).

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_output_fields_response = zapierembed.actions.get_output_fields(
    action="uag:87b1c14e-ef30-43d5-9395-6c6514dbb123",
    data={
        "authentication": None,
        "inputs": {},
        "fetch_live_samples": False,
    },
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### action: `str`<a id="action-str"></a>

An Action ID, as provided by the `/actions` endpoint.

##### data: [`InputsWithAuthenticationIdAndFetchLiveSamples`](./zapier_embed_python_sdk/type/inputs_with_authentication_id_and_fetch_live_samples.py)<a id="data-inputswithauthenticationidandfetchlivesampleszapier_embed_python_sdktypeinputs_with_authentication_id_and_fetch_live_samplespy"></a>


#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ActionsGetOutputFieldsRequest`](./zapier_embed_python_sdk/type/actions_get_output_fields_request.py)
Common inputs with inputs, an authentication id and a parameter to optionally retrieve live samples for the field

#### 🔄 Return<a id="🔄-return"></a>

[`ActionsGetOutputFieldsResponse`](./zapier_embed_python_sdk/pydantic/actions_get_output_fields_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/actions/{action}/outputs` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `zapierembed.actions.list_available_actions`<a id="zapierembedactionslist_available_actions"></a>

Fetch the available actions for the provided App. It's typical to filter by type so that only actions that make sense for a particular step are shown. For example only showing reads for the first step in a Zap.

This endpoint requires the `zap` OAuth scope.

This API is rate limited by IP address (60 requests per min), or partner (150 requests per min), whichever occurs first.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_available_actions_response = zapierembed.actions.list_available_actions(
    app="868f9d3c-2ea0-4f19-a32d-a61b276ab8de",
    action_type="READ",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### app: `str`<a id="app-str"></a>

A canonical App ID, as provided by the `/apps` endpoint.

##### action_type: `str`<a id="action_type-str"></a>

The type of Action to filter for.

#### 🔄 Return<a id="🔄-return"></a>

[`ActionsListAvailableActionsResponse`](./zapier_embed_python_sdk/pydantic/actions_list_available_actions_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/actions` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `zapierembed.actions.test_action_execution`<a id="zapierembedactionstest_action_execution"></a>

Tests the action (step) in the third party api, using the provided authentication and inputs. On a successful test returns 200 and the result of executing the action, otherwise it returns a 400 and details about the failure.

This endpoint requires the `zap:write` OAuth scope.

This API is rate limited by IP address (60 requests per min).

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
test_action_execution_response = zapierembed.actions.test_action_execution(
    action="action_example",
    data={
        "authentication": None,
    },
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### action: `str`<a id="action-str"></a>

An Action ID, as provided by the `/actions` endpoint.

##### data: [`InputsWithAuthenticationIdNoPage`](./zapier_embed_python_sdk/type/inputs_with_authentication_id_no_page.py)<a id="data-inputswithauthenticationidnopagezapier_embed_python_sdktypeinputs_with_authentication_id_no_pagepy"></a>


#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ActionsTestActionExecutionRequest`](./zapier_embed_python_sdk/type/actions_test_action_execution_request.py)
Authentication id and inputs (such as `worksheet`, `spreadsheet` for google sheets, `text` and `channel` for slack) used to test the action.

#### 🔄 Return<a id="🔄-return"></a>

[`ActionsTestActionExecutionResponse`](./zapier_embed_python_sdk/pydantic/actions_test_action_execution_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/actions/{action}/test` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `zapierembed.apps.list_popular`<a id="zapierembedappslist_popular"></a>

This endpoint returns a list of popular apps.  Keep in mind that Zapier built-in apps will not be returned and the order of the result is by app popularity.

This endpoint requires the `zap` OAuth scope.

This API is rate limited by IP address (60 requests per min), or partner (150 requests per min), whichever occurs first.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_popular_response = zapierembed.apps.list_popular(
    limit=1,
    offset=1,
    category="string_example",
    query="string_example",
    ids="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### limit: `int`<a id="limit-int"></a>

Used for paginating results. Specifies the amount of apps to return.

##### offset: `int`<a id="offset-int"></a>

Used for paginating results. Specifies the offset of the apps to return.

##### category: `str`<a id="category-str"></a>

Categories that apps must have in order to be returned in the response. E.g. Accounting (`accounting`), AI Tools (`ai-tools`), and All (`all`). The full list of valid categories can be retrieved using the `category` endpoint, detailed [here](https://platform.zapier.com/embed/partner-api#get-v1categories).

##### query: `str`<a id="query-str"></a>

Parameter to limit the results to apps whose titles match the provided query.

##### ids: `str`<a id="ids-str"></a>

Parameter to restrict the results to apps whose ID matches those in the provided comma-separated value. Cannot be combined with `category`.

#### 🔄 Return<a id="🔄-return"></a>

[`AppsListPopularResponse`](./zapier_embed_python_sdk/pydantic/apps_list_popular_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/apps` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `zapierembed.authentications.create_new_authentication`<a id="zapierembedauthenticationscreate_new_authentication"></a>

Creates a new Authentication for the provided App.

This endpoint requires the `authentication:write` OAuth scope.

This API is rate limited by IP address (60 requests per min), or partner (150 requests per min), whichever occurs first.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_authentication_response = (
    zapierembed.authentications.create_new_authentication(
        data={
            "title": "SuperExampleCRM (example@zapier.com)",
            "app": "868f9d3c-2ea0-4f19-a32d-a61b276ab8de",
            "authentication_fields": {},
        },
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### data: [`AuthenticationsCreateNewAuthenticationRequestData`](./zapier_embed_python_sdk/type/authentications_create_new_authentication_request_data.py)<a id="data-authenticationscreatenewauthenticationrequestdatazapier_embed_python_sdktypeauthentications_create_new_authentication_request_datapy"></a>


#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`AuthenticationsCreateNewAuthenticationRequest`](./zapier_embed_python_sdk/type/authentications_create_new_authentication_request.py)
Inputs to create a new Authentication

#### 🔄 Return<a id="🔄-return"></a>

[`AuthenticationsCreateNewAuthenticationResponse`](./zapier_embed_python_sdk/pydantic/authentications_create_new_authentication_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/authentications` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `zapierembed.authentications.get_available`<a id="zapierembedauthenticationsget_available"></a>

Fetch the available Authentications for the provided App. This will only return Authentications that are owned by the user and not those that are shared with them, since it''s not possible to create Zaps with Authentications you don''t own.

This endpoint requires the `authentication` OAuth scope.

This API is rate limited by IP address (60 requests per min), or partner (150 requests per min), whichever occurs first.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_available_response = zapierembed.authentications.get_available(
    app="868f9d3c-2ea0-4f19-a32d-a61b276ab8de",
    limit=10,
    offset=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### app: `str`<a id="app-str"></a>

A canonical App ID, as provided by the `/apps` endpoint.

##### limit: `int`<a id="limit-int"></a>

Used for paginating results. Specifies the maximum number of items to return per page. If this value is not set, it defaults to 10.

##### offset: `int`<a id="offset-int"></a>

Used for paginating results. Specifies the offset to use.

#### 🔄 Return<a id="🔄-return"></a>

[`AuthenticationsGetAvailableResponse`](./zapier_embed_python_sdk/pydantic/authentications_get_available_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/authentications` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `zapierembed.experimental.get_zap_runs`<a id="zapierembedexperimentalget_zap_runs"></a>

This endpoint is a first version tool that delivers basic yet essential details about their executed Zap runs. As an evolving interface, this first version serves foundational information about Zap runs.

_However, it's important to note that this is an initial implementation and the **response payload is not definitive**. Our aim is to continually iterate and enhance this API, refining its capabilities and data output, to progressively deliver more valuable and useful information in future versions._

This endpoint requires the `zap:runs` OAuth scope.

This API is rate limited by IP address (60 requests per min), or partner (150 requests per min), whichever occurs first.

Please note that since this is an experimental tool, if you're interested in gaining access, you must contact our support team.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_zap_runs_response = zapierembed.experimental.get_zap_runs(
    from_date="2024-01-01T10:09:08.07",
    to_date="2023-01-02T11:10:09.08",
    zap_id="001fa849-dc8e-aca6-a09b-ba705bceada1",
    limit=10,
    offset=10,
    search="string_example",
    statuses="throttled",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### from_date: `str`<a id="from_date-str"></a>

Find Zap runs equal to or newer than this date. If not provided, results default to last 30 days' Zap Runs.

##### to_date: `str`<a id="to_date-str"></a>

Find Zap runs less than this date.

##### zap_id: `str`<a id="zap_id-str"></a>

Find Zap runs for the specified Zap ID.

##### limit: `int`<a id="limit-int"></a>

Maximum number of returned Zap Runs.

##### offset: `int`<a id="offset-int"></a>

Number of Zap Runs to skip.

##### search: `str`<a id="search-str"></a>

Performs a text search against the `zap_title`, `data_in`, and `data_out` fields, returning only zap runs that match the specified keywords.

##### statuses: `str`<a id="statuses-str"></a>

Accepts one or more status values separated by commas, enabling the filtering of zap runs based on the specified status or statuses provided.

#### 🔄 Return<a id="🔄-return"></a>

[`ExperimentalGetZapRunsResponse`](./zapier_embed_python_sdk/pydantic/experimental_get_zap_runs_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/zap-runs` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `zapierembed.zaps.create_zap`<a id="zapierembedzapscreate_zap"></a>

This URL creates a new Zap based on a series of steps and a given title. `is_enabled` must be set to true when creating a new Zap.

This endpoint requires the `zap:write` OAuth scope.

This API is rate limited by IP address (60 requests per min), or partner (150 requests per min), whichever occurs first.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_zap_response = zapierembed.zaps.create_zap(
    items={
        "title": "My Zap",
        "type": "zap",
        "id": "00000000-0000-c000-8000-000000012345",
        "is_enabled": True,
        "steps": [
            {
                "action": None,
                "inputs": {},
                "authentication": None,
            }
        ],
        "updated_at": "2019-08-24T14:15:22Z",
    },
    expand="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### items: [`Zap`](./zapier_embed_python_sdk/type/zap.py)<a id="items-zapzapier_embed_python_sdktypezappy"></a>


##### expand: `str`<a id="expand-str"></a>

A comma separated list of Zap fields that should be expanded from ids to full objects in the response. If a field may not be expanded, its encoded form will be returned instead.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ZapsCreateZapRequest`](./zapier_embed_python_sdk/type/zaps_create_zap_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ZapsCreateZapResponse`](./zapier_embed_python_sdk/pydantic/zaps_create_zap_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/zaps` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `zapierembed.zaps.get_filtered_zaps`<a id="zapierembedzapsget_filtered_zaps"></a>

This endpoint returns a list of Zaps for the authenticated Zapier user.

The `expand` array can be used to expand selected fields into full objects in the response.  Inputs with keys can also be passed to filter Zaps by certain criteria.

This endpoint requires the `zap` OAuth scope.

This API is rate limited by IP address (60 requests per min), or partner (150 requests per min), whichever occurs first.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_filtered_zaps_response = zapierembed.zaps.get_filtered_zaps(
    limit=1,
    offset=1,
    inputs={
        "key": "string_example",
    },
    expand="steps.action",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### limit: `int`<a id="limit-int"></a>

Used for paginating results. Specifies the amount of apps to return

##### offset: `int`<a id="offset-int"></a>

Used for paginating results. Specifies the offset of the apps to return

##### inputs: [`Dict[str, str]`](./zapier_embed_python_sdk/type/.py)<a id="inputs-dictstr-strzapier_embed_python_sdktypepy"></a>

You may pass inputs[KEY]=VALUE1,VALUE2 to filter for Zaps that contain those settings. For example, if your OAuth app is Trello you may filter for Zaps that contain a certain Trello board using inputs[board]=BOARD_ID — Keys are defined by your app on the developer platform.

##### expand: `str`<a id="expand-str"></a>

A comma separated list of Zap fields that should be expanded from ids to full objects in the response. If a field may not be expanded, its encoded form will be returned instead.

#### 🔄 Return<a id="🔄-return"></a>

[`ZapsGetFilteredZapsResponse`](./zapier_embed_python_sdk/pydantic/zaps_get_filtered_zaps_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/zaps` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


## Author<a id="author"></a>
This Python package is automatically generated by [Konfig](https://konfigthis.com)
