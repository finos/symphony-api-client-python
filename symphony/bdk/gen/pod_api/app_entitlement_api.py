"""
    Pod API

    This document refers to Symphony API calls that do not need encryption or decryption of content.  - sessionToken can be obtained by calling the authenticationAPI on the symphony back end and the key manager respectively. Refer to the methods described in authenticatorAPI.yaml. - Actions are defined to be atomic, ie will succeed in their entirety or fail and have changed nothing. - If it returns a 40X status then it will have made no change to the system even if ome subset of the request would have succeeded. - If this contract cannot be met for any reason then this is an error and the response code will be 50X.   # noqa: E501

    The version of the OpenAPI document: 20.10.0
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from symphony.bdk.gen.api_client import ApiClient, Endpoint
from symphony.bdk.gen.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from symphony.bdk.gen.pod_model.error import Error
from symphony.bdk.gen.pod_model.pod_app_entitlement_list import PodAppEntitlementList
from symphony.bdk.gen.pod_model.user_app_entitlement_list import UserAppEntitlementList


class AppEntitlementApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __v1_admin_app_entitlement_list_get(
            self,
            session_token,
            **kwargs
        ):
            """Get the list of application entitlements for the company  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = pod_api.v1_admin_app_entitlement_list_get(session_token, async_req=True)
            >>> result = thread.get()

            Args:
                session_token (str): Session authentication token.

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
                PodAppEntitlementList
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
            return self.call_with_http_info(**kwargs)

        self.v1_admin_app_entitlement_list_get = Endpoint(
            settings={
                'response_type': (PodAppEntitlementList,),
                'auth': [],
                'endpoint_path': '/v1/admin/app/entitlement/list',
                'operation_id': 'v1_admin_app_entitlement_list_get',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'session_token',
                ],
                'required': [
                    'session_token',
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
                },
                'attribute_map': {
                    'session_token': 'sessionToken',
                },
                'location_map': {
                    'session_token': 'header',
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
            callable=__v1_admin_app_entitlement_list_get
        )

        def __v1_admin_app_entitlement_list_post(
            self,
            session_token,
            payload,
            **kwargs
        ):
            """Update the application entitlements for the company  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = pod_api.v1_admin_app_entitlement_list_post(session_token, payload, async_req=True)
            >>> result = thread.get()

            Args:
                session_token (str): Session authentication token.
                payload (PodAppEntitlementList):

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
                PodAppEntitlementList
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
            kwargs['payload'] = \
                payload
            return self.call_with_http_info(**kwargs)

        self.v1_admin_app_entitlement_list_post = Endpoint(
            settings={
                'response_type': (PodAppEntitlementList,),
                'auth': [],
                'endpoint_path': '/v1/admin/app/entitlement/list',
                'operation_id': 'v1_admin_app_entitlement_list_post',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'session_token',
                    'payload',
                ],
                'required': [
                    'session_token',
                    'payload',
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
                    'payload':
                        (PodAppEntitlementList,),
                },
                'attribute_map': {
                    'session_token': 'sessionToken',
                },
                'location_map': {
                    'session_token': 'header',
                    'payload': 'body',
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
            callable=__v1_admin_app_entitlement_list_post
        )

        def __v1_admin_user_uid_app_entitlement_list_get(
            self,
            session_token,
            uid,
            **kwargs
        ):
            """Get the list of application entitlements for this user  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = pod_api.v1_admin_user_uid_app_entitlement_list_get(session_token, uid, async_req=True)
            >>> result = thread.get()

            Args:
                session_token (str): Session authentication token.
                uid (int): User ID as a decimal integer

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
                UserAppEntitlementList
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
            kwargs['uid'] = \
                uid
            return self.call_with_http_info(**kwargs)

        self.v1_admin_user_uid_app_entitlement_list_get = Endpoint(
            settings={
                'response_type': (UserAppEntitlementList,),
                'auth': [],
                'endpoint_path': '/v1/admin/user/{uid}/app/entitlement/list',
                'operation_id': 'v1_admin_user_uid_app_entitlement_list_get',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'session_token',
                    'uid',
                ],
                'required': [
                    'session_token',
                    'uid',
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
                    'uid':
                        (int,),
                },
                'attribute_map': {
                    'session_token': 'sessionToken',
                    'uid': 'uid',
                },
                'location_map': {
                    'session_token': 'header',
                    'uid': 'path',
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
            callable=__v1_admin_user_uid_app_entitlement_list_get
        )

        def __v1_admin_user_uid_app_entitlement_list_post(
            self,
            session_token,
            uid,
            payload,
            **kwargs
        ):
            """Update the application entitlements for this user  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = pod_api.v1_admin_user_uid_app_entitlement_list_post(session_token, uid, payload, async_req=True)
            >>> result = thread.get()

            Args:
                session_token (str): Session authentication token.
                uid (int): User ID as a decimal integer
                payload (UserAppEntitlementList):

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
                UserAppEntitlementList
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
            kwargs['uid'] = \
                uid
            kwargs['payload'] = \
                payload
            return self.call_with_http_info(**kwargs)

        self.v1_admin_user_uid_app_entitlement_list_post = Endpoint(
            settings={
                'response_type': (UserAppEntitlementList,),
                'auth': [],
                'endpoint_path': '/v1/admin/user/{uid}/app/entitlement/list',
                'operation_id': 'v1_admin_user_uid_app_entitlement_list_post',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'session_token',
                    'uid',
                    'payload',
                ],
                'required': [
                    'session_token',
                    'uid',
                    'payload',
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
                    'uid':
                        (int,),
                    'payload':
                        (UserAppEntitlementList,),
                },
                'attribute_map': {
                    'session_token': 'sessionToken',
                    'uid': 'uid',
                },
                'location_map': {
                    'session_token': 'header',
                    'uid': 'path',
                    'payload': 'body',
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
            callable=__v1_admin_user_uid_app_entitlement_list_post
        )
