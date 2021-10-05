"""
    Agent API

    This document refers to Symphony API calls to send and receive messages and content. They need the on-premise Agent installed to perform decryption/encryption of content.  - sessionToken and keyManagerToken can be obtained by calling the authenticationAPI on the symphony back end and the key manager respectively. Refer to the methods described in authenticatorAPI.yaml. - Actions are defined to be atomic, ie will succeed in their entirety or fail and have changed nothing. - If it returns a 40X status then it will have sent no message to any stream even if a request to aome subset of the requested streams would have succeeded. - If this contract cannot be met for any reason then this is an error and the response code will be 50X. - MessageML is a markup language for messages. See reference here: https://rest-api.symphony.com/docs/messagemlv2 - **Real Time Events**: The following events are returned when reading from a real time messages and events stream (\"datafeed\"). These events will be returned for datafeeds created with the v5 endpoints. To know more about the endpoints, refer to Create Messages/Events Stream and Read Messages/Events Stream. Unless otherwise specified, all events were added in 1.46.   # noqa: E501

    The version of the OpenAPI document: 20.13.0
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
from symphony.bdk.gen.agent_model.ack_id import AckId
from symphony.bdk.gen.agent_model.datafeed import Datafeed
from symphony.bdk.gen.agent_model.v2_error import V2Error
from symphony.bdk.gen.agent_model.v4_event_list import V4EventList
from symphony.bdk.gen.agent_model.v5_datafeed import V5Datafeed
from symphony.bdk.gen.agent_model.v5_datafeed_create_body import V5DatafeedCreateBody
from symphony.bdk.gen.agent_model.v5_event_list import V5EventList


class DatafeedApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __create_datafeed(
            self,
            session_token,
            key_manager_token,
            **kwargs
        ):
            """Create a new real time messages / events stream (\"datafeed\").  # noqa: E501

            _Available on Agent 2.57.0 and above._  The datafeed provides messages and events from all conversations that the user is in. The types of events surfaced in the datafeed can be found in the Real Time Events list. (see definition on top of the file)  Returns the ID of the datafeed that has just been created. This ID should then be used as input to the Read Messages/Events Stream v4 endpoint.   # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = agent_api.create_datafeed(session_token, key_manager_token, async_req=True)
            >>> result = thread.get()

            Args:
                session_token (str): Session authentication token.
                key_manager_token (str): Key Manager authentication token.

            Keyword Args:
                body (V5DatafeedCreateBody): [optional]
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
                V5Datafeed
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
            return self.call_with_http_info(**kwargs)

        self.create_datafeed = _Endpoint(
            settings={
                'response_type': (V5Datafeed,),
                'auth': [],
                'endpoint_path': '/v5/datafeeds',
                'operation_id': 'create_datafeed',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'session_token',
                    'key_manager_token',
                    'body',
                ],
                'required': [
                    'session_token',
                    'key_manager_token',
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
                    'body':
                        (V5DatafeedCreateBody,),
                },
                'attribute_map': {
                    'session_token': 'sessionToken',
                    'key_manager_token': 'keyManagerToken',
                },
                'location_map': {
                    'session_token': 'header',
                    'key_manager_token': 'header',
                    'body': 'body',
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
            callable=__create_datafeed
        )

        def __delete_datafeed(
            self,
            datafeed_id,
            session_token,
            key_manager_token,
            **kwargs
        ):
            """Delete the specified real time message / event stream (\"datafeed\").  # noqa: E501

            _Available on Agent 2.57.0 and above._  The datafeed provides messages and events from all conversations that the user is in. The types of events surfaced in the datafeed can be found in the Real Time Events list. (see definition on top of the file)  Delete the specified datafeed.   # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = agent_api.delete_datafeed(datafeed_id, session_token, key_manager_token, async_req=True)
            >>> result = thread.get()

            Args:
                datafeed_id (str): ID of the datafeed
                session_token (str): Session authentication token.
                key_manager_token (str): Key Manager authentication token.

            Keyword Args:
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
                V2Error
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
            kwargs['datafeed_id'] = \
                datafeed_id
            kwargs['session_token'] = \
                session_token
            kwargs['key_manager_token'] = \
                key_manager_token
            return self.call_with_http_info(**kwargs)

        self.delete_datafeed = _Endpoint(
            settings={
                'response_type': (V2Error,),
                'auth': [],
                'endpoint_path': '/v5/datafeeds/{datafeedId}',
                'operation_id': 'delete_datafeed',
                'http_method': 'DELETE',
                'servers': None,
            },
            params_map={
                'all': [
                    'datafeed_id',
                    'session_token',
                    'key_manager_token',
                ],
                'required': [
                    'datafeed_id',
                    'session_token',
                    'key_manager_token',
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
                    'datafeed_id':
                        (str,),
                    'session_token':
                        (str,),
                    'key_manager_token':
                        (str,),
                },
                'attribute_map': {
                    'datafeed_id': 'datafeedId',
                    'session_token': 'sessionToken',
                    'key_manager_token': 'keyManagerToken',
                },
                'location_map': {
                    'datafeed_id': 'path',
                    'session_token': 'header',
                    'key_manager_token': 'header',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    '*/*'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__delete_datafeed
        )

        def __list_datafeed(
            self,
            session_token,
            key_manager_token,
            **kwargs
        ):
            """Read list of real time messages / events stream (\"datafeed\").  # noqa: E501

            _Available on Agent 2.57.0 and above._  The datafeed provides messages and events from all conversations that the user is in. The types of events surfaced in the datafeed can be found in the [Real Time Events](./docs/real-time-events.md) list.  Returns the list of the datafeeds for the user. Any datafeed ID of the list can then be used as input to the Read Messages/Events Stream v4 endpoint.   # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = agent_api.list_datafeed(session_token, key_manager_token, async_req=True)
            >>> result = thread.get()

            Args:
                session_token (str): Session authentication token.
                key_manager_token (str): Key Manager authentication token.

            Keyword Args:
                tag (str): A unique identifier to ensure uniqueness of the datafeed. Used to restrict search.. [optional]
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
                [V5Datafeed]
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
            return self.call_with_http_info(**kwargs)

        self.list_datafeed = _Endpoint(
            settings={
                'response_type': ([V5Datafeed],),
                'auth': [],
                'endpoint_path': '/v5/datafeeds',
                'operation_id': 'list_datafeed',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'session_token',
                    'key_manager_token',
                    'tag',
                ],
                'required': [
                    'session_token',
                    'key_manager_token',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                    'tag',
                ]
            },
            root_map={
                'validations': {
                    ('tag',): {
                        'max_length': 100,
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'session_token':
                        (str,),
                    'key_manager_token':
                        (str,),
                    'tag':
                        (str,),
                },
                'attribute_map': {
                    'session_token': 'sessionToken',
                    'key_manager_token': 'keyManagerToken',
                    'tag': 'tag',
                },
                'location_map': {
                    'session_token': 'header',
                    'key_manager_token': 'header',
                    'tag': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json',
                    '200 OK'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__list_datafeed
        )

        def __read_datafeed(
            self,
            datafeed_id,
            session_token,
            key_manager_token,
            **kwargs
        ):
            """Read the specified real time message / event stream (\"datafeed\").  # noqa: E501

            _Available on Agent 2.57.0 and above._  The datafeed provides messages and events from all conversations that the user is in. The types of events surfaced in the datafeed can be found in the Real Time Events list. (see definition on top of the file)  Read the specified datafeed.  The ackId sent as parameter can be empty for the first call. In the response an ackId will be sent back and it can be used for the next call: in this way you acknowledge that you have received the events that came with that ackId; datafeed will remove the events associated with that ackId from your queue   # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = agent_api.read_datafeed(datafeed_id, session_token, key_manager_token, async_req=True)
            >>> result = thread.get()

            Args:
                datafeed_id (str): ID of the datafeed
                session_token (str): Session authentication token.
                key_manager_token (str): Key Manager authentication token.

            Keyword Args:
                ack_id (AckId): ackId received from last POST Base64 encoded.. [optional]
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
                V5EventList
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
            kwargs['datafeed_id'] = \
                datafeed_id
            kwargs['session_token'] = \
                session_token
            kwargs['key_manager_token'] = \
                key_manager_token
            return self.call_with_http_info(**kwargs)

        self.read_datafeed = _Endpoint(
            settings={
                'response_type': (V5EventList,),
                'auth': [],
                'endpoint_path': '/v5/datafeeds/{datafeedId}/read',
                'operation_id': 'read_datafeed',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'datafeed_id',
                    'session_token',
                    'key_manager_token',
                    'ack_id',
                ],
                'required': [
                    'datafeed_id',
                    'session_token',
                    'key_manager_token',
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
                    'datafeed_id':
                        (str,),
                    'session_token':
                        (str,),
                    'key_manager_token':
                        (str,),
                    'ack_id':
                        (AckId,),
                },
                'attribute_map': {
                    'datafeed_id': 'datafeedId',
                    'session_token': 'sessionToken',
                    'key_manager_token': 'keyManagerToken',
                },
                'location_map': {
                    'datafeed_id': 'path',
                    'session_token': 'header',
                    'key_manager_token': 'header',
                    'ack_id': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client,
            callable=__read_datafeed
        )

        def __v4_datafeed_create_post(
            self,
            session_token,
            key_manager_token,
            **kwargs
        ):
            """Create a new real time message event stream.  # noqa: E501

            A datafeed provides the messages in all conversations that a user is in. This also includes system messages like new users joining a chatroom.  A datafeed will expire if it isn't read before its capacity is reached.   # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = agent_api.v4_datafeed_create_post(session_token, key_manager_token, async_req=True)
            >>> result = thread.get()

            Args:
                session_token (str): Session authentication token.
                key_manager_token (str): Key Manager authentication token.

            Keyword Args:
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
                Datafeed
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
            return self.call_with_http_info(**kwargs)

        self.v4_datafeed_create_post = _Endpoint(
            settings={
                'response_type': (Datafeed,),
                'auth': [],
                'endpoint_path': '/v4/datafeed/create',
                'operation_id': 'v4_datafeed_create_post',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'session_token',
                    'key_manager_token',
                ],
                'required': [
                    'session_token',
                    'key_manager_token',
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
                },
                'attribute_map': {
                    'session_token': 'sessionToken',
                    'key_manager_token': 'keyManagerToken',
                },
                'location_map': {
                    'session_token': 'header',
                    'key_manager_token': 'header',
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
            callable=__v4_datafeed_create_post
        )

        def __v4_datafeed_id_read_get(
            self,
            id,
            session_token,
            key_manager_token,
            **kwargs
        ):
            """Read a given datafeed.  # noqa: E501

            Read messages from the given datafeed. If no more messages are available then this method will block. It is intended that the client should re-call this method as soon as it has processed the messages received in the previous call. If the client is able to consume messages more quickly than they become available then each call will initially block, there is no need to delay before re-calling this method.  A datafeed will expire if its unread capacity is reached. A datafeed can only be consumed by one client thread at a time. E.g. polling the datafeed by two threads may lead to messages being delivered out of order.   # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = agent_api.v4_datafeed_id_read_get(id, session_token, key_manager_token, async_req=True)
            >>> result = thread.get()

            Args:
                id (str): Datafeed ID 
                session_token (str): Session authentication token.
                key_manager_token (str): Key Manager authentication token.

            Keyword Args:
                limit (int): Max No. of messages to return. . [optional]
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
                V4EventList
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
            kwargs['id'] = \
                id
            kwargs['session_token'] = \
                session_token
            kwargs['key_manager_token'] = \
                key_manager_token
            return self.call_with_http_info(**kwargs)

        self.v4_datafeed_id_read_get = _Endpoint(
            settings={
                'response_type': (V4EventList,),
                'auth': [],
                'endpoint_path': '/v4/datafeed/{id}/read',
                'operation_id': 'v4_datafeed_id_read_get',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'id',
                    'session_token',
                    'key_manager_token',
                    'limit',
                ],
                'required': [
                    'id',
                    'session_token',
                    'key_manager_token',
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
                    'id':
                        (str,),
                    'session_token':
                        (str,),
                    'key_manager_token':
                        (str,),
                    'limit':
                        (int,),
                },
                'attribute_map': {
                    'id': 'id',
                    'session_token': 'sessionToken',
                    'key_manager_token': 'keyManagerToken',
                    'limit': 'limit',
                },
                'location_map': {
                    'id': 'path',
                    'session_token': 'header',
                    'key_manager_token': 'header',
                    'limit': 'query',
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
            callable=__v4_datafeed_id_read_get
        )
