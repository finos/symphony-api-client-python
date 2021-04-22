"""
    Pod API

    This document refers to Symphony API calls that do not need encryption or decryption of content.  - sessionToken can be obtained by calling the authenticationAPI on the symphony back end and the key manager respectively. Refer to the methods described in authenticatorAPI.yaml. - Actions are defined to be atomic, ie will succeed in their entirety or fail and have changed nothing. - If it returns a 40X status then it will have made no change to the system even if ome subset of the request would have succeeded. - If this contract cannot be met for any reason then this is an error and the response code will be 50X.   # noqa: E501

    The version of the OpenAPI document: 20.12.1
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
from symphony.bdk.gen.pod_model.bulk_action_result import BulkActionResult
from symphony.bdk.gen.pod_model.error import Error
from symphony.bdk.gen.pod_model.group_list import GroupList
from symphony.bdk.gen.pod_model.integer_list import IntegerList
from symphony.bdk.gen.pod_model.policy_list import PolicyList


class InfoBarriersApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __v1_admin_group_gid_membership_add_post(
            self,
            gid,
            session_token,
            users,
            **kwargs
        ):
            """Add members to an Information Barrier group.  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = pod_api.v1_admin_group_gid_membership_add_post(gid, session_token, users, async_req=True)
            >>> result = thread.get()

            Args:
                gid (str): URL-Safe encoded Group ID
                session_token (str): Session authentication token.
                users (IntegerList):

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
                BulkActionResult
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
            kwargs['gid'] = \
                gid
            kwargs['session_token'] = \
                session_token
            kwargs['users'] = \
                users
            return self.call_with_http_info(**kwargs)

        self.v1_admin_group_gid_membership_add_post = _Endpoint(
            settings={
                'response_type': (BulkActionResult,),
                'auth': [],
                'endpoint_path': '/v1/admin/group/{gid}/membership/add',
                'operation_id': 'v1_admin_group_gid_membership_add_post',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'gid',
                    'session_token',
                    'users',
                ],
                'required': [
                    'gid',
                    'session_token',
                    'users',
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
                    'gid':
                        (str,),
                    'session_token':
                        (str,),
                    'users':
                        (IntegerList,),
                },
                'attribute_map': {
                    'gid': 'gid',
                    'session_token': 'sessionToken',
                },
                'location_map': {
                    'gid': 'path',
                    'session_token': 'header',
                    'users': 'body',
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
            callable=__v1_admin_group_gid_membership_add_post
        )

        def __v1_admin_group_gid_membership_list_get(
            self,
            gid,
            session_token,
            **kwargs
        ):
            """Get the list of userids in this Information Barrier Group  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = pod_api.v1_admin_group_gid_membership_list_get(gid, session_token, async_req=True)
            >>> result = thread.get()

            Args:
                gid (str): URL-Safe encoded Group ID
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
                IntegerList
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
            kwargs['gid'] = \
                gid
            kwargs['session_token'] = \
                session_token
            return self.call_with_http_info(**kwargs)

        self.v1_admin_group_gid_membership_list_get = _Endpoint(
            settings={
                'response_type': (IntegerList,),
                'auth': [],
                'endpoint_path': '/v1/admin/group/{gid}/membership/list',
                'operation_id': 'v1_admin_group_gid_membership_list_get',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'gid',
                    'session_token',
                ],
                'required': [
                    'gid',
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
                    'gid':
                        (str,),
                    'session_token':
                        (str,),
                },
                'attribute_map': {
                    'gid': 'gid',
                    'session_token': 'sessionToken',
                },
                'location_map': {
                    'gid': 'path',
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
            callable=__v1_admin_group_gid_membership_list_get
        )

        def __v1_admin_group_gid_membership_remove_post(
            self,
            gid,
            session_token,
            users,
            **kwargs
        ):
            """Remove members from an Information Barrier group  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = pod_api.v1_admin_group_gid_membership_remove_post(gid, session_token, users, async_req=True)
            >>> result = thread.get()

            Args:
                gid (str): URL-Safe encoded Group ID
                session_token (str): Session authentication token.
                users (IntegerList):

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
                BulkActionResult
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
            kwargs['gid'] = \
                gid
            kwargs['session_token'] = \
                session_token
            kwargs['users'] = \
                users
            return self.call_with_http_info(**kwargs)

        self.v1_admin_group_gid_membership_remove_post = _Endpoint(
            settings={
                'response_type': (BulkActionResult,),
                'auth': [],
                'endpoint_path': '/v1/admin/group/{gid}/membership/remove',
                'operation_id': 'v1_admin_group_gid_membership_remove_post',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'gid',
                    'session_token',
                    'users',
                ],
                'required': [
                    'gid',
                    'session_token',
                    'users',
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
                    'gid':
                        (str,),
                    'session_token':
                        (str,),
                    'users':
                        (IntegerList,),
                },
                'attribute_map': {
                    'gid': 'gid',
                    'session_token': 'sessionToken',
                },
                'location_map': {
                    'gid': 'path',
                    'session_token': 'header',
                    'users': 'body',
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
            callable=__v1_admin_group_gid_membership_remove_post
        )

        def __v1_admin_group_list_get(
            self,
            session_token,
            **kwargs
        ):
            """Get a list of all Information Barrier Groups  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = pod_api.v1_admin_group_list_get(session_token, async_req=True)
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
                GroupList
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

        self.v1_admin_group_list_get = _Endpoint(
            settings={
                'response_type': (GroupList,),
                'auth': [],
                'endpoint_path': '/v1/admin/group/list',
                'operation_id': 'v1_admin_group_list_get',
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
            callable=__v1_admin_group_list_get
        )

        def __v1_admin_policy_list_get(
            self,
            session_token,
            **kwargs
        ):
            """Get all Information Policies  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = pod_api.v1_admin_policy_list_get(session_token, async_req=True)
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
                PolicyList
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

        self.v1_admin_policy_list_get = _Endpoint(
            settings={
                'response_type': (PolicyList,),
                'auth': [],
                'endpoint_path': '/v1/admin/policy/list',
                'operation_id': 'v1_admin_policy_list_get',
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
            callable=__v1_admin_policy_list_get
        )
