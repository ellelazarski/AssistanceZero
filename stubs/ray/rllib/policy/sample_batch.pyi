import builtins
from typing import Any, Dict, Iterator, Union, overload

from _typeshed import Incomplete
from ray.rllib.utils.annotations import DeveloperAPI as DeveloperAPI
from ray.rllib.utils.annotations import ExperimentalAPI as ExperimentalAPI
from ray.rllib.utils.annotations import PublicAPI as PublicAPI
from ray.rllib.utils.compression import is_compressed as is_compressed
from ray.rllib.utils.compression import pack as pack
from ray.rllib.utils.compression import unpack as unpack
from ray.rllib.utils.deprecation import Deprecated as Deprecated
from ray.rllib.utils.deprecation import deprecation_warning as deprecation_warning
from ray.rllib.utils.framework import try_import_tf as try_import_tf
from ray.rllib.utils.framework import try_import_torch as try_import_torch
from ray.rllib.utils.torch_utils import (
    convert_to_torch_tensor as convert_to_torch_tensor,
)
from ray.rllib.utils.typing import PolicyID as PolicyID
from ray.rllib.utils.typing import SampleBatchType as SampleBatchType
from ray.rllib.utils.typing import TensorType as TensorType
from ray.rllib.utils.typing import ViewRequirementsDict as ViewRequirementsDict
from ray.util import log_once as log_once

tf1: Incomplete
tf: Incomplete
tfv: Incomplete
torch: Incomplete
_: Incomplete
DEFAULT_POLICY_ID: str

def attempt_count_timesteps(tensor_dict: dict): ...

class SampleBatch(dict):
    OBS: str
    NEXT_OBS: str
    ACTIONS: str
    REWARDS: str
    PREV_ACTIONS: str
    PREV_REWARDS: str
    TERMINATEDS: str
    TRUNCATEDS: str
    INFOS: str
    SEQ_LENS: str
    T: str
    EPS_ID: str
    ENV_ID: str
    AGENT_INDEX: str
    UNROLL_ID: str
    ACTION_DIST_INPUTS: str
    ACTION_PROB: str
    ACTION_LOGP: str
    ACTION_DIST: str
    VF_PREDS: str
    VALUES_BOOTSTRAPPED: str
    OBS_EMBEDS: str
    RETURNS_TO_GO: str
    ATTENTION_MASKS: str
    DONES: str
    CUR_OBS: str
    time_major: bool
    max_seq_len: int
    zero_padded: bool
    num_grad_updates: Incomplete
    accessed_keys: Incomplete
    added_keys: Incomplete
    deleted_keys: Incomplete
    intercepted_values: Incomplete
    get_interceptor: Incomplete
    count: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...
    def __len__(self) -> int: ...
    def agent_steps(self) -> int: ...
    def env_steps(self) -> int: ...
    def enable_slicing_by_batch_id(self) -> None: ...
    def disable_slicing_by_batch_id(self) -> None: ...
    def is_terminated_or_truncated(self) -> bool: ...
    def is_single_trajectory(self) -> bool: ...
    @staticmethod
    def concat_samples(
        samples: list["SampleBatch"] | list["MultiAgentBatch"],
    ) -> SampleBatch | MultiAgentBatch: ...
    def concat(self, other: SampleBatch) -> SampleBatch: ...
    def copy(self, shallow: bool = False) -> SampleBatch: ...
    def rows(self) -> Iterator[dict[str, TensorType]]: ...
    def columns(self, keys: list[str]) -> list[Any]: ...
    def shuffle(self) -> SampleBatch: ...
    def split_by_episode(self, key: str | None = None) -> list["SampleBatch"]: ...
    def slice(
        self,
        start: int,
        end: int,
        state_start: Incomplete | None = None,
        state_end: Incomplete | None = None,
    ) -> SampleBatch: ...
    def timeslices(
        self,
        size: int | None = None,
        num_slices: int | None = None,
        k: int | None = None,
    ) -> list["SampleBatch"]: ...
    def zero_pad(self, max_seq_len, exclude_states: bool = True): ...
    def right_zero_pad(self, max_seq_len: int, exclude_states: bool = True): ...
    def to_device(self, device, framework: str = "torch"): ...
    def size_bytes(self) -> int: ...
    def get(self, key, default: Incomplete | None = None): ...
    def as_multi_agent(self) -> MultiAgentBatch: ...
    def __getitem__(self, key: Union[str, builtins.slice]) -> TensorType: ...
    def __setitem__(self, key, item) -> None: ...
    @property
    def is_training(self): ...
    def set_training(self, training: Union[bool, tf1.placeholder] = True): ...
    def __delitem__(self, key) -> None: ...
    def compress(self, bulk: bool = False, columns: set[str] = ...) -> SampleBatch: ...
    def decompress_if_needed(self, columns: set[str] = ...) -> SampleBatch: ...
    def set_get_interceptor(self, fn) -> None: ...
    def get_single_step_input_dict(
        self, view_requirements: ViewRequirementsDict, index: str | int = "last"
    ) -> SampleBatch: ...

class MultiAgentBatch:
    policy_batches: Dict[PolicyID, SampleBatch]
    count: int
    def __init__(
        self, policy_batches: dict[PolicyID, SampleBatch], env_steps: int
    ) -> None: ...
    def env_steps(self) -> int: ...
    def __len__(self) -> int: ...
    def agent_steps(self) -> int: ...
    def timeslices(self, k: int) -> list["MultiAgentBatch"]: ...
    @staticmethod
    def wrap_as_needed(
        policy_batches: dict[PolicyID, SampleBatch], env_steps: int
    ) -> SampleBatch | MultiAgentBatch: ...
    @staticmethod
    def concat_samples(samples: list["MultiAgentBatch"]) -> MultiAgentBatch: ...
    def copy(self) -> MultiAgentBatch: ...
    def size_bytes(self) -> int: ...
    def compress(self, bulk: bool = False, columns: set[str] = ...) -> None: ...
    def decompress_if_needed(self, columns: set[str] = ...) -> MultiAgentBatch: ...
    def as_multi_agent(self) -> MultiAgentBatch: ...
    def __getitem__(self, key: str) -> SampleBatch: ...

@overload
def concat_samples(samples: list[SampleBatch]) -> SampleBatch: ...
@overload
def concat_samples(samples: list[MultiAgentBatch]) -> MultiAgentBatch: ...
@overload
def concat_samples(samples: list[SampleBatchType]) -> SampleBatchType: ...
def concat_samples_into_ma_batch(samples: list[SampleBatchType]) -> MultiAgentBatch: ...
def convert_ma_batch_to_sample_batch(batch: SampleBatchType) -> SampleBatch: ...
