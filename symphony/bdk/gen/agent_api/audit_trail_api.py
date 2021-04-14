"""
    Agent API

    This document refers to Symphony API calls to send and receive messages and content. They need the on-premise Agent installed to perform decryption/encryption of content.  - sessionToken and keyManagerToken can be obtained by calling the authenticationAPI on the symphony back end and the key manager respectively. Refer to the methods described in authenticatorAPI.yaml. - Actions are defined to be atomic, ie will succeed in their entirety or fail and have changed nothing. - If it returns a 40X status then it will have sent no message to any stream even if a request to aome subset of the requested streams would have succeeded. - If this contract cannot be met for any reason then this is an error and the response code will be 50X. - MessageML is a markup language for messages. See reference here: https://rest-api.symphony.com/docs/messagemlv2 - **Real Time Events**: The following events are returned when reading from a real time messages and events stream (\"datafeed\"). These events will be returned for datafeeds created with the v5 endpoints. To know more about the endpoints, refer to Create Messages/Events Stream and Read Messages/Events Stream. Unless otherwise specified, all events were added in 1.46.   # noqa: E501

    The version of the OpenAPI document: 20.12.0
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from symphony.bdk.gen.api_client import ApiClient, Endpoint as _Endpoint
from symphony.bdk.gen.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from symphony.bdk.gen.agent_model.error import Error
from symphony.bdk.gen.agent_model.v1_audit_trail_initiator_list import V1AuditTrailInitiatorList


class AuditTrailApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __v1_audittrail_privilegeduser_get(
            self,
            session_token,
            key_manager_token,
            start_timestamp,
            **kwargs
        ):
            """Get a list of  actions performed by a privileged account acting as privileged user given a period of time.  # noqa: E501

            Get a list of actions performed by a privileged account acting as privileged user given a period of time.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = agent_api.v1_audittrail_privilegeduser_get(session_token, key_manager_token, start_timestamp, async_req=True)
            >>> result = thread.get()

            Args:
                session_token (str): Session authentication token.
                key_manager_token (str): Key Manager authentication token.
                start_timestamp (int): Start timestamp in unix timestamp in millseconds. 

            Keyword Args:
                end_timestamp (int): End timestamp in unix timestamp in millseconds. If not specified, it assumes to be current time. . [optional]
                before (str): Return results from an opaque “before” cursor value as presented via a response cursor. . [optional]
                after (str): Return results from an opaque “after” cursor value as presented via a response cursor. . [optional]
                limit (int): Max No. of violations to return. If no value is provided, 50 is the default. Some maximums for limit may be enforced for performance reasons. The maximum supported value is 500. . [optional]
                initiator_id (int): If present, only the initiator with this initiator <user id> will be returned. . [optional]
                role (str): If present, only the audit trail initiated by s user with privileged role acting as privileged user will be returned. Privileged eliglible roles: User Provisioning (USER_PROVISIONING), Content Management (CONTENT_MANAGEMENT), Expression Filter Policy Management (EF_POLICY_MANAGEMENT), SCO (SUPER_COMPLIANCE_OFFICER), CO (COMPLIANCE_OFFICER), Super admin (SUPER_ADMINISTRATOR), Admin (ADMINISTRATOR), L1 (L1_SUPPORT), L2 (L2_SUPPORT), Scope Manager (SCOPE_MANAGEMENT) . [optional]
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                V1AuditTrailInitiatorList
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['session_token'] = \
                session_token
            kwargs['key_manager_token'] = \
                key_manager_token
            kwargs['start_timestamp'] = \
                start_timestamp
            return self.call_with_http_info(**kwargs)

        self.v1_audittrail_privilegeduser_get = _Endpoint(
            settings={
                'response_type': (V1AuditTrailInitiatorList,),
                'auth': [],
                'endpoint_path': '/v1/audittrail/privilegeduser',
                'operation_id': 'v1_audittrail_privilegeduser_get',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'session_token',
                    'key_manager_token',
                    'start_timestamp',
                    'end_timestamp',
                    'before',
                    'after',
                    'limit',
                    'initiator_id',
                    'role',
                ],
                'required': [
                    'session_token',
                    'key_manager_token',
                    'start_timestamp',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'session_token':
                        (str,),
                    'key_manager_token':
                        (str,),
                    'start_timestamp':
                        (int,),
                    'end_timestamp':
                        (int,),
                    'before':
                        (str,),
                    'after':
                        (str,),
                    'limit':
                        (int,),
                    'initiator_id':
                        (int,),
                    'role':
                        (str,),
                },
                'attribute_map': {
                    'session_token': 'sessionToken',
                    'key_manager_token': 'keyManagerToken',
                    'start_timestamp': 'startTimestamp',
                    'end_timestamp': 'endTimestamp',
                    'before': 'before',
                    'after': 'after',
                    'limit': 'limit',
                    'initiator_id': 'initiatorId',
                    'role': 'role',
                },
                'location_map': {
                    'session_token': 'header',
                    'key_manager_token': 'header',
                    'start_timestamp': 'query',
                    'end_timestamp': 'query',
                    'before': 'query',
                    'after': 'query',
                    'limit': 'query',
                    'initiator_id': 'query',
                    'role': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__v1_audittrail_privilegeduser_get
        )
