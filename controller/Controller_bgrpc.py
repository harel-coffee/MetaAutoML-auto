# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: Common.proto, ControllerService.proto, DatasetRelatedMessages.proto, Enumerations.proto, ModelRelatedMessages.proto, TestingRelatedMessages.proto, TrainingRelatedMessages.proto, UserRelatedMessages.proto, WizzardMessages.proto
# plugin: python-betterproto
from dataclasses import dataclass
from datetime import datetime
from typing import (
    TYPE_CHECKING,
    Dict,
    List,
    Optional,
)

import betterproto
import grpclib
from betterproto.grpc.grpclib_server import ServiceBase


if TYPE_CHECKING:
    from betterproto.grpc.grpclib_client import MetadataLike
    from grpclib.metadata import Deadline


class ResultCode(betterproto.Enum):
    RESULT_CODE_OKAY = 0
    RESULT_CODE_ERROR_CAN_NOT_CREATE_USER = 1


class DataType(betterproto.Enum):
    DATATYPE_UNKNOW = 0
    DATATYPE_STRING = 1
    DATATYPE_INT = 2
    DATATYPE_FLOAT = 3
    DATATYPE_CATEGORY = 4
    DATATYPE_BOOLEAN = 5
    DATATYPE_DATETIME = 6
    DATATYPE_IGNORE = 7


class DatasetType(betterproto.Enum):
    DATASET_TYPE_UNKNOWN = 0
    DATASET_TYPE_TABULAR_DATA = 1


class ControllerReturnCode(betterproto.Enum):
    CONTROLLER_RETURN_CODE_UNKNOWN = 0
    CONTROLLER_RETURN_CODE_SUCCESS = 1
    CONTROLLER_RETURN_CODE_STATUS_UPDATE = 2
    CONTROLLER_RETURN_CODE_ERROR = 100


class SessionStatus(betterproto.Enum):
    SESSION_STATUS_UNKNOWN = 0
    SESSION_STATUS_BUSY = 1
    SESSION_STATUS_COMPLETED = 2
    SESSION_STATUS_FAILED = 3


class SplitMethod(betterproto.Enum):
    SPLIT_METHOD_RANDOM = 0
    SPLIT_METHOD_END = 1


@dataclass(eq=False, repr=False)
class TestConfiguration(betterproto.Message):
    split_ratio: float = betterproto.float_field(1)
    method: "SplitMethod" = betterproto.enum_field(2)
    random_state: int = betterproto.int32_field(3)


@dataclass(eq=False, repr=False)
class AutoMlTarget(betterproto.Message):
    target: str = betterproto.string_field(1)
    type: "DataType" = betterproto.enum_field(2)


@dataclass(eq=False, repr=False)
class GetObjectsInformationRequest(betterproto.Message):
    ids: List[str] = betterproto.string_field(1)


@dataclass(eq=False, repr=False)
class GetObjectsInformationResponse(betterproto.Message):
    object_informations: List["ObjectInformation"] = betterproto.message_field(1)


@dataclass(eq=False, repr=False)
class ObjectInformation(betterproto.Message):
    id: str = betterproto.string_field(1)
    informations: Dict[str, str] = betterproto.map_field(
        2, betterproto.TYPE_STRING, betterproto.TYPE_STRING
    )


@dataclass(eq=False, repr=False)
class GetDatasetTypesRequest(betterproto.Message):
    pass


@dataclass(eq=False, repr=False)
class GetDatasetTypesResponse(betterproto.Message):
    dataset_types: List[str] = betterproto.string_field(1)


@dataclass(eq=False, repr=False)
class GetDatasetsRequest(betterproto.Message):
    username: str = betterproto.string_field(1)
    type: "DatasetType" = betterproto.enum_field(2)


@dataclass(eq=False, repr=False)
class GetDatasetsResponse(betterproto.Message):
    dataset: List["Dataset"] = betterproto.message_field(1)


@dataclass(eq=False, repr=False)
class Dataset(betterproto.Message):
    name: str = betterproto.string_field(1)
    type: str = betterproto.string_field(2)
    creation_date: datetime = betterproto.message_field(3)
    identifier: str = betterproto.string_field(4)
    size: int = betterproto.int64_field(5)
    analysis: str = betterproto.string_field(6)


@dataclass(eq=False, repr=False)
class GetDatasetRequest(betterproto.Message):
    username: str = betterproto.string_field(1)
    identifier: str = betterproto.string_field(2)


@dataclass(eq=False, repr=False)
class GetDatasetResponse(betterproto.Message):
    dataset_infos: "Dataset" = betterproto.message_field(1)


@dataclass(eq=False, repr=False)
class TableColumn(betterproto.Message):
    name: str = betterproto.string_field(1)
    type: "DataType" = betterproto.enum_field(2)
    convertible_types: List["DataType"] = betterproto.enum_field(3)
    first_entries: List[str] = betterproto.string_field(4)


@dataclass(eq=False, repr=False)
class GetTabularDatasetColumnRequest(betterproto.Message):
    username: str = betterproto.string_field(1)
    dataset_identifier: str = betterproto.string_field(2)


@dataclass(eq=False, repr=False)
class GetTabularDatasetColumnResponse(betterproto.Message):
    columns: List["TableColumn"] = betterproto.message_field(1)


@dataclass(eq=False, repr=False)
class UploadDatasetFileRequest(betterproto.Message):
    username: str = betterproto.string_field(1)
    file_name: str = betterproto.string_field(2)
    dataset_name: str = betterproto.string_field(3)
    type: str = betterproto.string_field(4)


@dataclass(eq=False, repr=False)
class UploadDatasetFileResponse(betterproto.Message):
    return_code: int = betterproto.int32_field(1)


@dataclass(eq=False, repr=False)
class GetAutoMlModelRequest(betterproto.Message):
    username: str = betterproto.string_field(1)
    training_id: str = betterproto.string_field(2)
    auto_ml: str = betterproto.string_field(3)


@dataclass(eq=False, repr=False)
class GetAutoMlModelResponse(betterproto.Message):
    name: str = betterproto.string_field(1)
    file: bytes = betterproto.bytes_field(2)


@dataclass(eq=False, repr=False)
class GetModelsRequest(betterproto.Message):
    username: str = betterproto.string_field(1)
    dataset_id: str = betterproto.string_field(2)
    top3: bool = betterproto.bool_field(3)


@dataclass(eq=False, repr=False)
class GetModelsResponse(betterproto.Message):
    models: List["ModelInformation"] = betterproto.message_field(1)


@dataclass(eq=False, repr=False)
class GetModelRequest(betterproto.Message):
    username: str = betterproto.string_field(1)
    model_id: str = betterproto.string_field(2)


@dataclass(eq=False, repr=False)
class GetModelResponse(betterproto.Message):
    model: "ModelInformation" = betterproto.message_field(1)


@dataclass(eq=False, repr=False)
class ModelInformation(betterproto.Message):
    identifier: str = betterproto.string_field(1)
    training_id: str = betterproto.string_field(2)
    test_score: float = betterproto.float_field(3)
    validation_score: float = betterproto.float_field(4)
    runtime: int = betterproto.int32_field(5)
    model: str = betterproto.string_field(6)
    library: str = betterproto.string_field(7)
    status: str = betterproto.string_field(8)
    status_messages: List[str] = betterproto.string_field(9)
    prediction_time: float = betterproto.float_field(10)
    automl: str = betterproto.string_field(11)
    dataset_id: str = betterproto.string_field(12)


@dataclass(eq=False, repr=False)
class GetAllTrainingsRequest(betterproto.Message):
    username: str = betterproto.string_field(1)


@dataclass(eq=False, repr=False)
class GetAllTrainingsResponse(betterproto.Message):
    trainings: List["GetTrainingResponse"] = betterproto.message_field(1)


@dataclass(eq=False, repr=False)
class GetTrainingsRequest(betterproto.Message):
    username: str = betterproto.string_field(1)


@dataclass(eq=False, repr=False)
class GetTrainingsResponse(betterproto.Message):
    training_ids: List[str] = betterproto.string_field(1)


@dataclass(eq=False, repr=False)
class GetTrainingRequest(betterproto.Message):
    username: str = betterproto.string_field(1)
    id: str = betterproto.string_field(2)


@dataclass(eq=False, repr=False)
class GetTrainingResponse(betterproto.Message):
    status: str = betterproto.string_field(1)
    automls: List["AutoMlStatus"] = betterproto.message_field(2)
    dataset_id: str = betterproto.string_field(3)
    dataset_name: str = betterproto.string_field(4)
    task: str = betterproto.string_field(5)
    configuration: str = betterproto.string_field(6)
    required_ml_libraries: List[str] = betterproto.string_field(7)
    required_auto_mls: List[str] = betterproto.string_field(8)
    runtime_constraints: str = betterproto.string_field(9)
    dataset_configuration: str = betterproto.string_field(10)
    identifier: str = betterproto.string_field(11)
    start_time: datetime = betterproto.message_field(12)


@dataclass(eq=False, repr=False)
class AutoMlStatus(betterproto.Message):
    name: str = betterproto.string_field(1)
    status: str = betterproto.string_field(2)
    messages: List[str] = betterproto.string_field(3)
    test_score: float = betterproto.float_field(4)
    validation_score: float = betterproto.float_field(5)
    runtime: int = betterproto.int32_field(6)
    predictiontime: float = betterproto.float_field(7)
    library: str = betterproto.string_field(8)
    model: str = betterproto.string_field(9)
    identifier: str = betterproto.string_field(10)


@dataclass(eq=False, repr=False)
class TestAutoMlRequest(betterproto.Message):
    username: str = betterproto.string_field(1)
    test_data: bytes = betterproto.bytes_field(2)
    model_id: str = betterproto.string_field(3)


@dataclass(eq=False, repr=False)
class TestAutoMlResponse(betterproto.Message):
    predictions: List[str] = betterproto.string_field(1)
    score: float = betterproto.float_field(2)
    predictiontime: float = betterproto.float_field(3)


@dataclass(eq=False, repr=False)
class CreateNewUserRequest(betterproto.Message):
    pass


@dataclass(eq=False, repr=False)
class CreateNewUserResponse(betterproto.Message):
    result: "ResultCode" = betterproto.enum_field(1)
    oma_ml_user_id: str = betterproto.string_field(2)


@dataclass(eq=False, repr=False)
class GetCompatibleAutoMlSolutionsRequest(betterproto.Message):
    username: str = betterproto.string_field(1)
    configuration: Dict[str, str] = betterproto.map_field(
        2, betterproto.TYPE_STRING, betterproto.TYPE_STRING
    )


@dataclass(eq=False, repr=False)
class GetCompatibleAutoMlSolutionsResponse(betterproto.Message):
    auto_ml_solutions: List[str] = betterproto.string_field(1)


@dataclass(eq=False, repr=False)
class GetDatasetCompatibleTasksRequest(betterproto.Message):
    username: str = betterproto.string_field(1)
    dataset_name: str = betterproto.string_field(2)


@dataclass(eq=False, repr=False)
class GetDatasetCompatibleTasksResponse(betterproto.Message):
    tasks: List[str] = betterproto.string_field(1)


@dataclass(eq=False, repr=False)
class GetSupportedMlLibrariesRequest(betterproto.Message):
    username: str = betterproto.string_field(1)
    task: str = betterproto.string_field(2)


@dataclass(eq=False, repr=False)
class GetSupportedMlLibrariesResponse(betterproto.Message):
    ml_libraries: List[str] = betterproto.string_field(1)


@dataclass(eq=False, repr=False)
class StartAutoMlProcessRequest(betterproto.Message):
    username: str = betterproto.string_field(1)
    dataset: str = betterproto.string_field(2)
    task: str = betterproto.string_field(3)
    configuration: str = betterproto.string_field(4)
    required_auto_mls: List[str] = betterproto.string_field(5)
    runtime_constraints: str = betterproto.string_field(6)
    dataset_configuration: str = betterproto.string_field(7)
    test_configuration: str = betterproto.string_field(8)
    file_configuration: str = betterproto.string_field(9)
    metric: str = betterproto.string_field(10)
    required_libraries: List[str] = betterproto.string_field(11)


@dataclass(eq=False, repr=False)
class StartAutoMlProcessResponse(betterproto.Message):
    result: "ControllerReturnCode" = betterproto.enum_field(1)
    training_id: str = betterproto.string_field(2)


class ControllerServiceStub(betterproto.ServiceStub):
    async def create_new_user(
        self,
        create_new_user_request: "CreateNewUserRequest",
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["_MetadataLike"] = None,
    ) -> "CreateNewUserResponse":
        return await self._unary_unary(
            "/ControllerService/CreateNewUser",
            create_new_user_request,
            CreateNewUserResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def get_auto_ml_model(
        self,
        get_auto_ml_model_request: "GetAutoMlModelRequest",
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["_MetadataLike"] = None,
    ) -> "GetAutoMlModelResponse":
        return await self._unary_unary(
            "/ControllerService/GetAutoMlModel",
            get_auto_ml_model_request,
            GetAutoMlModelResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def get_compatible_auto_ml_solutions(
        self,
        get_compatible_auto_ml_solutions_request: "GetCompatibleAutoMlSolutionsRequest",
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["_MetadataLike"] = None,
    ) -> "GetCompatibleAutoMlSolutionsResponse":
        return await self._unary_unary(
            "/ControllerService/GetCompatibleAutoMlSolutions",
            get_compatible_auto_ml_solutions_request,
            GetCompatibleAutoMlSolutionsResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def get_dataset_types(
        self,
        get_dataset_types_request: "GetDatasetTypesRequest",
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["_MetadataLike"] = None,
    ) -> "GetDatasetTypesResponse":
        return await self._unary_unary(
            "/ControllerService/GetDatasetTypes",
            get_dataset_types_request,
            GetDatasetTypesResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def get_datasets(
        self,
        get_datasets_request: "GetDatasetsRequest",
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["_MetadataLike"] = None,
    ) -> "GetDatasetsResponse":
        return await self._unary_unary(
            "/ControllerService/GetDatasets",
            get_datasets_request,
            GetDatasetsResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def get_dataset(
        self,
        get_dataset_request: "GetDatasetRequest",
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["_MetadataLike"] = None,
    ) -> "GetDatasetResponse":
        return await self._unary_unary(
            "/ControllerService/GetDataset",
            get_dataset_request,
            GetDatasetResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def get_trainings(
        self,
        get_trainings_request: "GetTrainingsRequest",
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["_MetadataLike"] = None,
    ) -> "GetTrainingsResponse":
        return await self._unary_unary(
            "/ControllerService/GetTrainings",
            get_trainings_request,
            GetTrainingsResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def get_training(
        self,
        get_training_request: "GetTrainingRequest",
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["_MetadataLike"] = None,
    ) -> "GetTrainingResponse":
        return await self._unary_unary(
            "/ControllerService/GetTraining",
            get_training_request,
            GetTrainingResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def get_all_trainings(
        self,
        get_all_trainings_request: "GetAllTrainingsRequest",
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["_MetadataLike"] = None,
    ) -> "GetAllTrainingsResponse":
        return await self._unary_unary(
            "/ControllerService/GetAllTrainings",
            get_all_trainings_request,
            GetAllTrainingsResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def get_supported_ml_libraries(
        self,
        get_supported_ml_libraries_request: "GetSupportedMlLibrariesRequest",
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["_MetadataLike"] = None,
    ) -> "GetSupportedMlLibrariesResponse":
        return await self._unary_unary(
            "/ControllerService/GetSupportedMlLibraries",
            get_supported_ml_libraries_request,
            GetSupportedMlLibrariesResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def get_tabular_dataset_column(
        self,
        get_tabular_dataset_column_request: "GetTabularDatasetColumnRequest",
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["_MetadataLike"] = None,
    ) -> "GetTabularDatasetColumnResponse":
        return await self._unary_unary(
            "/ControllerService/GetTabularDatasetColumn",
            get_tabular_dataset_column_request,
            GetTabularDatasetColumnResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def get_dataset_compatible_tasks(
        self,
        get_dataset_compatible_tasks_request: "GetDatasetCompatibleTasksRequest",
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["_MetadataLike"] = None,
    ) -> "GetDatasetCompatibleTasksResponse":
        return await self._unary_unary(
            "/ControllerService/GetDatasetCompatibleTasks",
            get_dataset_compatible_tasks_request,
            GetDatasetCompatibleTasksResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def get_models(
        self,
        get_models_request: "GetModelsRequest",
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["_MetadataLike"] = None,
    ) -> "GetModelsResponse":
        return await self._unary_unary(
            "/ControllerService/GetModels",
            get_models_request,
            GetModelsResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def get_model(
        self,
        get_model_request: "GetModelRequest",
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["_MetadataLike"] = None,
    ) -> "GetModelResponse":
        return await self._unary_unary(
            "/ControllerService/GetModel",
            get_model_request,
            GetModelResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def get_objects_information(
        self,
        get_objects_information_request: "GetObjectsInformationRequest",
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["_MetadataLike"] = None,
    ) -> "GetObjectsInformationResponse":
        return await self._unary_unary(
            "/ControllerService/GetObjectsInformation",
            get_objects_information_request,
            GetObjectsInformationResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def upload_dataset_file(
        self,
        upload_dataset_file_request: "UploadDatasetFileRequest",
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["_MetadataLike"] = None,
    ) -> "UploadDatasetFileResponse":
        return await self._unary_unary(
            "/ControllerService/UploadDatasetFile",
            upload_dataset_file_request,
            UploadDatasetFileResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def start_auto_ml_process(
        self,
        start_auto_ml_process_request: "StartAutoMlProcessRequest",
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["_MetadataLike"] = None,
    ) -> "StartAutoMlProcessResponse":
        return await self._unary_unary(
            "/ControllerService/StartAutoMlProcess",
            start_auto_ml_process_request,
            StartAutoMlProcessResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def test_auto_ml(
        self,
        test_auto_ml_request: "TestAutoMlRequest",
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["_MetadataLike"] = None,
    ) -> "TestAutoMlResponse":
        return await self._unary_unary(
            "/ControllerService/TestAutoML",
            test_auto_ml_request,
            TestAutoMlResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )


class ControllerServiceBase(ServiceBase):
    async def create_new_user(
        self, create_new_user_request: "CreateNewUserRequest"
    ) -> "CreateNewUserResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def get_auto_ml_model(
        self, get_auto_ml_model_request: "GetAutoMlModelRequest"
    ) -> "GetAutoMlModelResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def get_compatible_auto_ml_solutions(
        self,
        get_compatible_auto_ml_solutions_request: "GetCompatibleAutoMlSolutionsRequest",
    ) -> "GetCompatibleAutoMlSolutionsResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def get_dataset_types(
        self, get_dataset_types_request: "GetDatasetTypesRequest"
    ) -> "GetDatasetTypesResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def get_datasets(
        self, get_datasets_request: "GetDatasetsRequest"
    ) -> "GetDatasetsResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def get_dataset(
        self, get_dataset_request: "GetDatasetRequest"
    ) -> "GetDatasetResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def get_trainings(
        self, get_trainings_request: "GetTrainingsRequest"
    ) -> "GetTrainingsResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def get_training(
        self, get_training_request: "GetTrainingRequest"
    ) -> "GetTrainingResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def get_all_trainings(
        self, get_all_trainings_request: "GetAllTrainingsRequest"
    ) -> "GetAllTrainingsResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def get_supported_ml_libraries(
        self, get_supported_ml_libraries_request: "GetSupportedMlLibrariesRequest"
    ) -> "GetSupportedMlLibrariesResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def get_tabular_dataset_column(
        self, get_tabular_dataset_column_request: "GetTabularDatasetColumnRequest"
    ) -> "GetTabularDatasetColumnResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def get_dataset_compatible_tasks(
        self, get_dataset_compatible_tasks_request: "GetDatasetCompatibleTasksRequest"
    ) -> "GetDatasetCompatibleTasksResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def get_models(
        self, get_models_request: "GetModelsRequest"
    ) -> "GetModelsResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def get_model(
        self, get_model_request: "GetModelRequest"
    ) -> "GetModelResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def get_objects_information(
        self, get_objects_information_request: "GetObjectsInformationRequest"
    ) -> "GetObjectsInformationResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def upload_dataset_file(
        self, upload_dataset_file_request: "UploadDatasetFileRequest"
    ) -> "UploadDatasetFileResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def start_auto_ml_process(
        self, start_auto_ml_process_request: "StartAutoMlProcessRequest"
    ) -> "StartAutoMlProcessResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def test_auto_ml(
        self, test_auto_ml_request: "TestAutoMlRequest"
    ) -> "TestAutoMlResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def __rpc_create_new_user(self, stream: grpclib.server.Stream) -> None:
        request = await stream.recv_message()
        response = await self.create_new_user(request)
        await stream.send_message(response)

    async def __rpc_get_auto_ml_model(self, stream: grpclib.server.Stream) -> None:
        request = await stream.recv_message()
        response = await self.get_auto_ml_model(request)
        await stream.send_message(response)

    async def __rpc_get_compatible_auto_ml_solutions(
        self, stream: grpclib.server.Stream
    ) -> None:
        request = await stream.recv_message()
        response = await self.get_compatible_auto_ml_solutions(request)
        await stream.send_message(response)

    async def __rpc_get_dataset_types(self, stream: grpclib.server.Stream) -> None:
        request = await stream.recv_message()
        response = await self.get_dataset_types(request)
        await stream.send_message(response)

    async def __rpc_get_datasets(self, stream: grpclib.server.Stream) -> None:
        request = await stream.recv_message()
        response = await self.get_datasets(request)
        await stream.send_message(response)

    async def __rpc_get_dataset(self, stream: grpclib.server.Stream) -> None:
        request = await stream.recv_message()
        response = await self.get_dataset(request)
        await stream.send_message(response)

    async def __rpc_get_trainings(self, stream: grpclib.server.Stream) -> None:
        request = await stream.recv_message()
        response = await self.get_trainings(request)
        await stream.send_message(response)

    async def __rpc_get_training(self, stream: grpclib.server.Stream) -> None:
        request = await stream.recv_message()
        response = await self.get_training(request)
        await stream.send_message(response)

    async def __rpc_get_all_trainings(self, stream: grpclib.server.Stream) -> None:
        request = await stream.recv_message()
        response = await self.get_all_trainings(request)
        await stream.send_message(response)

    async def __rpc_get_supported_ml_libraries(
        self, stream: grpclib.server.Stream
    ) -> None:
        request = await stream.recv_message()
        response = await self.get_supported_ml_libraries(request)
        await stream.send_message(response)

    async def __rpc_get_tabular_dataset_column(
        self, stream: grpclib.server.Stream
    ) -> None:
        request = await stream.recv_message()
        response = await self.get_tabular_dataset_column(request)
        await stream.send_message(response)

    async def __rpc_get_dataset_compatible_tasks(
        self, stream: grpclib.server.Stream
    ) -> None:
        request = await stream.recv_message()
        response = await self.get_dataset_compatible_tasks(request)
        await stream.send_message(response)

    async def __rpc_get_models(self, stream: grpclib.server.Stream) -> None:
        request = await stream.recv_message()
        response = await self.get_models(request)
        await stream.send_message(response)

    async def __rpc_get_model(self, stream: grpclib.server.Stream) -> None:
        request = await stream.recv_message()
        response = await self.get_model(request)
        await stream.send_message(response)

    async def __rpc_get_objects_information(
        self, stream: grpclib.server.Stream
    ) -> None:
        request = await stream.recv_message()
        response = await self.get_objects_information(request)
        await stream.send_message(response)

    async def __rpc_upload_dataset_file(self, stream: grpclib.server.Stream) -> None:
        request = await stream.recv_message()
        response = await self.upload_dataset_file(request)
        await stream.send_message(response)

    async def __rpc_start_auto_ml_process(self, stream: grpclib.server.Stream) -> None:
        request = await stream.recv_message()
        response = await self.start_auto_ml_process(request)
        await stream.send_message(response)

    async def __rpc_test_auto_ml(self, stream: grpclib.server.Stream) -> None:
        request = await stream.recv_message()
        response = await self.test_auto_ml(request)
        await stream.send_message(response)

    def __mapping__(self) -> Dict[str, grpclib.const.Handler]:
        return {
            "/ControllerService/CreateNewUser": grpclib.const.Handler(
                self.__rpc_create_new_user,
                grpclib.const.Cardinality.UNARY_UNARY,
                CreateNewUserRequest,
                CreateNewUserResponse,
            ),
            "/ControllerService/GetAutoMlModel": grpclib.const.Handler(
                self.__rpc_get_auto_ml_model,
                grpclib.const.Cardinality.UNARY_UNARY,
                GetAutoMlModelRequest,
                GetAutoMlModelResponse,
            ),
            "/ControllerService/GetCompatibleAutoMlSolutions": grpclib.const.Handler(
                self.__rpc_get_compatible_auto_ml_solutions,
                grpclib.const.Cardinality.UNARY_UNARY,
                GetCompatibleAutoMlSolutionsRequest,
                GetCompatibleAutoMlSolutionsResponse,
            ),
            "/ControllerService/GetDatasetTypes": grpclib.const.Handler(
                self.__rpc_get_dataset_types,
                grpclib.const.Cardinality.UNARY_UNARY,
                GetDatasetTypesRequest,
                GetDatasetTypesResponse,
            ),
            "/ControllerService/GetDatasets": grpclib.const.Handler(
                self.__rpc_get_datasets,
                grpclib.const.Cardinality.UNARY_UNARY,
                GetDatasetsRequest,
                GetDatasetsResponse,
            ),
            "/ControllerService/GetDataset": grpclib.const.Handler(
                self.__rpc_get_dataset,
                grpclib.const.Cardinality.UNARY_UNARY,
                GetDatasetRequest,
                GetDatasetResponse,
            ),
            "/ControllerService/GetTrainings": grpclib.const.Handler(
                self.__rpc_get_trainings,
                grpclib.const.Cardinality.UNARY_UNARY,
                GetTrainingsRequest,
                GetTrainingsResponse,
            ),
            "/ControllerService/GetTraining": grpclib.const.Handler(
                self.__rpc_get_training,
                grpclib.const.Cardinality.UNARY_UNARY,
                GetTrainingRequest,
                GetTrainingResponse,
            ),
            "/ControllerService/GetAllTrainings": grpclib.const.Handler(
                self.__rpc_get_all_trainings,
                grpclib.const.Cardinality.UNARY_UNARY,
                GetAllTrainingsRequest,
                GetAllTrainingsResponse,
            ),
            "/ControllerService/GetSupportedMlLibraries": grpclib.const.Handler(
                self.__rpc_get_supported_ml_libraries,
                grpclib.const.Cardinality.UNARY_UNARY,
                GetSupportedMlLibrariesRequest,
                GetSupportedMlLibrariesResponse,
            ),
            "/ControllerService/GetTabularDatasetColumn": grpclib.const.Handler(
                self.__rpc_get_tabular_dataset_column,
                grpclib.const.Cardinality.UNARY_UNARY,
                GetTabularDatasetColumnRequest,
                GetTabularDatasetColumnResponse,
            ),
            "/ControllerService/GetDatasetCompatibleTasks": grpclib.const.Handler(
                self.__rpc_get_dataset_compatible_tasks,
                grpclib.const.Cardinality.UNARY_UNARY,
                GetDatasetCompatibleTasksRequest,
                GetDatasetCompatibleTasksResponse,
            ),
            "/ControllerService/GetModels": grpclib.const.Handler(
                self.__rpc_get_models,
                grpclib.const.Cardinality.UNARY_UNARY,
                GetModelsRequest,
                GetModelsResponse,
            ),
            "/ControllerService/GetModel": grpclib.const.Handler(
                self.__rpc_get_model,
                grpclib.const.Cardinality.UNARY_UNARY,
                GetModelRequest,
                GetModelResponse,
            ),
            "/ControllerService/GetObjectsInformation": grpclib.const.Handler(
                self.__rpc_get_objects_information,
                grpclib.const.Cardinality.UNARY_UNARY,
                GetObjectsInformationRequest,
                GetObjectsInformationResponse,
            ),
            "/ControllerService/UploadDatasetFile": grpclib.const.Handler(
                self.__rpc_upload_dataset_file,
                grpclib.const.Cardinality.UNARY_UNARY,
                UploadDatasetFileRequest,
                UploadDatasetFileResponse,
            ),
            "/ControllerService/StartAutoMlProcess": grpclib.const.Handler(
                self.__rpc_start_auto_ml_process,
                grpclib.const.Cardinality.UNARY_UNARY,
                StartAutoMlProcessRequest,
                StartAutoMlProcessResponse,
            ),
            "/ControllerService/TestAutoML": grpclib.const.Handler(
                self.__rpc_test_auto_ml,
                grpclib.const.Cardinality.UNARY_UNARY,
                TestAutoMlRequest,
                TestAutoMlResponse,
            ),
        }
