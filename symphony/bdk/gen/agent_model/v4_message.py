"""
    Agent API

    This document refers to Symphony API calls to send and receive messages and content. They need the on-premise Agent installed to perform decryption/encryption of content.  - sessionToken and keyManagerToken can be obtained by calling the authenticationAPI on the symphony back end and the key manager respectively. Refer to the methods described in authenticatorAPI.yaml. - A new authorizationToken has been introduced in the authenticationAPI response payload. It can be used to replace the sessionToken in any of the API calls and can be passed as \"Authorization\" header. - Actions are defined to be atomic, ie will succeed in their entirety or fail and have changed nothing. - If it returns a 40X status then it will have sent no message to any stream even if a request to some subset of the requested streams would have succeeded. - If this contract cannot be met for any reason then this is an error and the response code will be 50X. - MessageML is a markup language for messages. See reference here: https://rest-api.symphony.com/docs/messagemlv2 - **Real Time Events**: The following events are returned when reading from a real time messages and events stream (\"datafeed\"). These events will be returned for datafeeds created with the v5 endpoints. To know more about the endpoints, refer to Create Messages/Events Stream and Read Messages/Events Stream. Unless otherwise specified, all events were added in 1.46.   # noqa: E501

    The version of the OpenAPI document: 20.15.0-SNAPSHOT
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401
from typing import List, Union

from symphony.bdk.gen.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
    OpenApiModel
)
from symphony.bdk.gen.exceptions import ApiAttributeError


from symphony.bdk.gen.agent_model.v4_attachment_info import V4AttachmentInfo
from symphony.bdk.gen.agent_model.v4_stream import V4Stream
from symphony.bdk.gen.agent_model.v4_user import V4User
globals()['V4AttachmentInfo'] = V4AttachmentInfo
globals()['V4Stream'] = V4Stream
globals()['V4User'] = V4User

class V4Message(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
    }

    validations = {
    }

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a agent_model may have properties that are
        of type self, this must run after the class is loaded
        """
        return (bool, date, datetime, dict, float, int, list, str, none_type,)  # noqa: E501

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a agent_model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        return {
            'message_id': (str, none_type),  # noqa: E501
            'timestamp': (int, none_type),  # noqa: E501
            'message': (str, none_type),  # noqa: E501
            'shared_message': (V4Message, none_type),  # noqa: E501
            'data': (str, none_type),  # noqa: E501
            'attachments': ([V4AttachmentInfo], none_type),  # noqa: E501
            'user': (V4User, none_type),  # noqa: E501
            'stream': (V4Stream, none_type),  # noqa: E501
            'external_recipients': (bool, none_type),  # noqa: E501
            'diagnostic': (str, none_type),  # noqa: E501
            'user_agent': (str, none_type),  # noqa: E501
            'original_format': (str, none_type),  # noqa: E501
            'disclaimer': (str, none_type),  # noqa: E501
            'sid': (str, none_type),  # noqa: E501
            'replacing': (str, none_type),  # noqa: E501
            'replaced_by': (str, none_type),  # noqa: E501
            'initial_timestamp': (int, none_type),  # noqa: E501
            'initial_message_id': (str, none_type),  # noqa: E501
            'silent': (bool, none_type),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'message_id': 'messageId',  # noqa: E501
        'timestamp': 'timestamp',  # noqa: E501
        'message': 'message',  # noqa: E501
        'shared_message': 'sharedMessage',  # noqa: E501
        'data': 'data',  # noqa: E501
        'attachments': 'attachments',  # noqa: E501
        'user': 'user',  # noqa: E501
        'stream': 'stream',  # noqa: E501
        'external_recipients': 'externalRecipients',  # noqa: E501
        'diagnostic': 'diagnostic',  # noqa: E501
        'user_agent': 'userAgent',  # noqa: E501
        'original_format': 'originalFormat',  # noqa: E501
        'disclaimer': 'disclaimer',  # noqa: E501
        'sid': 'sid',  # noqa: E501
        'replacing': 'replacing',  # noqa: E501
        'replaced_by': 'replacedBy',  # noqa: E501
        'initial_timestamp': 'initialTimestamp',  # noqa: E501
        'initial_message_id': 'initialMessageId',  # noqa: E501
        'silent': 'silent',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """V4Message - a agent_model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the agent_model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            message_id (str): Id of the message. [optional]  # noqa: E501
            timestamp (int): Timestamp of the message in milliseconds since Jan 1 1970. [optional]  # noqa: E501
            message (str): Message content in MessageMLV2. [optional]  # noqa: E501
            shared_message (V4Message): [optional]  # noqa: E501
            data (str): Message data in EntityJSON. [optional]  # noqa: E501
            attachments ([V4AttachmentInfo]): Message attachments. [optional]  # noqa: E501
            user (V4User): [optional]  # noqa: E501
            stream (V4Stream): [optional]  # noqa: E501
            external_recipients (bool): Indicates if the message have external recipients. Only present on real time messaging.. [optional]  # noqa: E501
            diagnostic (str): Details if event failed to parse for any reason.  The contents of this field may not be useful, depending on the nature of the error. Only present when error occurs. . [optional]  # noqa: E501
            user_agent (str): User agent string for client that sent the message.  Allows callers to identify which client sent the origin message (e.g. API Agent, SFE Client, mobile, etc) . [optional]  # noqa: E501
            original_format (str): Indicates the format in which the message was originally sent.  This could have been either: - com.symphony.markdown - Markdown OR Message ML V1 - com.symphony.messageml.v2 - Message ML V2 . [optional]  # noqa: E501
            disclaimer (str): Message that may be sent along with a regular message if configured for the POD, usually the first message sent in a room that day. . [optional]  # noqa: E501
            sid (str): Unique session identifier from where the message was created. . [optional]  # noqa: E501
            replacing (str): Id of the message that the current message is replacing (present only if set). [optional]  # noqa: E501
            replaced_by (str): Id of the message that the current message is being replaced with (present only if set). [optional]  # noqa: E501
            initial_timestamp (int): Timestamp of when the initial message has been created in milliseconds since Jan 1 1970 (present only if set). [optional]  # noqa: E501
            initial_message_id (str): Id the the initial message that has been updated (present only if set). [optional]  # noqa: E501
            silent (bool): When false the user/s will receive the message update as unread (true by default).. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
        return self

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, *args, **kwargs):  # noqa: E501
        """V4Message - a agent_model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the agent_model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            message_id (str): Id of the message. [optional]  # noqa: E501
            timestamp (int): Timestamp of the message in milliseconds since Jan 1 1970. [optional]  # noqa: E501
            message (str): Message content in MessageMLV2. [optional]  # noqa: E501
            shared_message (V4Message): [optional]  # noqa: E501
            data (str): Message data in EntityJSON. [optional]  # noqa: E501
            attachments ([V4AttachmentInfo]): Message attachments. [optional]  # noqa: E501
            user (V4User): [optional]  # noqa: E501
            stream (V4Stream): [optional]  # noqa: E501
            external_recipients (bool): Indicates if the message have external recipients. Only present on real time messaging.. [optional]  # noqa: E501
            diagnostic (str): Details if event failed to parse for any reason.  The contents of this field may not be useful, depending on the nature of the error. Only present when error occurs. . [optional]  # noqa: E501
            user_agent (str): User agent string for client that sent the message.  Allows callers to identify which client sent the origin message (e.g. API Agent, SFE Client, mobile, etc) . [optional]  # noqa: E501
            original_format (str): Indicates the format in which the message was originally sent.  This could have been either: - com.symphony.markdown - Markdown OR Message ML V1 - com.symphony.messageml.v2 - Message ML V2 . [optional]  # noqa: E501
            disclaimer (str): Message that may be sent along with a regular message if configured for the POD, usually the first message sent in a room that day. . [optional]  # noqa: E501
            sid (str): Unique session identifier from where the message was created. . [optional]  # noqa: E501
            replacing (str): Id of the message that the current message is replacing (present only if set). [optional]  # noqa: E501
            replaced_by (str): Id of the message that the current message is being replaced with (present only if set). [optional]  # noqa: E501
            initial_timestamp (int): Timestamp of when the initial message has been created in milliseconds since Jan 1 1970 (present only if set). [optional]  # noqa: E501
            initial_message_id (str): Id the the initial message that has been updated (present only if set). [optional]  # noqa: E501
            silent (bool): When false the user/s will receive the message update as unread (true by default).. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.message_id: str = None
        self.timestamp: int = None
        self.message: str = None
        self.shared_message: V4Message = None
        self.data: str = None
        self.attachments: List[V4AttachmentInfo] = None
        self.user: V4User = None
        self.stream: V4Stream = None
        self.external_recipients: bool = None
        self.diagnostic: str = None
        self.user_agent: str = None
        self.original_format: str = None
        self.disclaimer: str = None
        self.sid: str = None
        self.replacing: str = None
        self.replaced_by: str = None
        self.initial_timestamp: int = None
        self.initial_message_id: str = None
        self.silent: bool = None
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                                     f"class with read only attributes.")
