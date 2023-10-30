from typing import Any, Callable, Dict, List, Optional, Sequence, Tuple, Union
from abc import abstractmethod
from datapipes.datapipe import DataPipe
import uuid

class Memory(DataPipe):

  data: Dict[str, Dict]
  def store(self, data):
    key = uuid.uuid4()
    self.data[key] = data
    return key
  
  def retrieve(self, key):
    if key not in self.data:
      raise ValueError(
        f"The data with the key {key} does not exist."
      )
    return self.data[key]
    