from typing import Any, Callable, Dict, List, Literal, Optional, Type

from attr import AttrsInstance
from starlette.routing import BaseRoute
from starlette.schemas import EndpointInfo

from bentoml import Service
from openllm_core._typing_compat import ParamSpec

P = ParamSpec('P')

class OpenLLMSchemaGenerator:
  base_schema: Dict[str, Any]
  def get_endpoints(self, routes: list[BaseRoute]) -> list[EndpointInfo]: ...
  def get_schema(self, routes: list[BaseRoute], mount_path: Optional[str] = ...) -> Dict[str, Any]: ...
  def parse_docstring(self, func_or_method: Callable[P, Any]) -> Dict[str, Any]: ...

def add_schema_definitions(func: Callable[P, Any]) -> Callable[P, Any]: ...
def append_schemas(
  svc: Service, generated_schema: Dict[str, Any], tags_order: Literal['prepend', 'append'] = ..., inject: bool = ...
) -> Service: ...
def component_schema_generator(attr_cls: Type[AttrsInstance], description: Optional[str] = ...) -> Dict[str, Any]: ...
def get_generator(
  title: str,
  components: Optional[List[Type[AttrsInstance]]] = ...,
  tags: Optional[List[Dict[str, Any]]] = ...,
  inject: bool = ...,
) -> OpenLLMSchemaGenerator: ...
