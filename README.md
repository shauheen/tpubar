# TPUBar

 Google Cloud TPU Utilization Bar for Training Models
 
<p align="center">
    <br>
    <img src="docs/tpubar_img.png"/>
    <br>
<p>


```shell
pip install --upgrade git+https://github.com/trisongz/tpubar.git
```

## Quickstart

```python3

!pip install --upgrade git+https://github.com/trisongz/tpubar.git

# Option #1 on Colab

!tpubar test # you will be prompted to authenticate with GCE on Colab

# Option #2 on Colab

from google.colab import auth
from tpubar import TPUMonitor
import os

auth.authenticate_user()

monitor = TPUMonitor(tpu_name=os.environ.get('TPU_NAME', None), profiler='v2')

# your training code below

monitor.start()

for x in dataset:
    ops(x)
    print(monitor.current_stats)

# Option #3 in Terminal/CLI - (Non Colab/Remote VM/Your Desktop)
tpubar test tpu-name

```

## API Quickstart

```python3
from tpubar import TPUMonitor

'''
default args
- tpu_name = None, (str) name of a TPU you want to query, in case of multiple active TPUs
- project = None, (str) gcp project name
- profiler = 'v1', (str) options are ['v1', 'v2']
    - v1: for Non-Colab, Pytorch, Tensorflow Estimator (TF1), and Non-Tensorflow TPU Queries
    - v2: Colab, Tensorflow 2+
- refresh_secs = 10, (int) how many seconds between each query
- fileout = None, (str) path where tqdm goes to, defaults to sys.stdout
- verbose = False, (bool) prints current_stats every query if True
- disable = False, (bool) disables TPU Bars if True, useful if only stats want to be captured

# Colors can be defined using standard cli colors or hex (e.g. 'green' or ' #00 ff00')
- tpu_util = 'green', (str) color for TPU MXU Bar
- tpu_secondary = 'yellow', (str) color for second TPU Bar [Memory for v1, Active Time for v2]
- cpu_util = 'blue', (str) color for CPU Utilization Bar
- ram_util = 'blue' (str) color for RAM Utilization Bar

'''
monitor = TPUMonitor(tpu_name=None, project=None, profiler='v1', refresh_secs=10, fileout=None, verbose=False, disable=False, tpu_util='green', tpu_secondary='yellow', cpu_util='blue', ram_util='blue')

monitor.start()

# Can be called to retrieve stats, use stats.get(var, '') to avoid errors since Idle Time and Idle String don't return anything until after full TPU initialization.
'''
# Stats available

- v1 returns {'tpu_mxu': float, 'tpu_mem_per': float 'tpu_mem_used': float, 'tpu_mem_str': str, 'cpu_util': float, 'ram_util': float, 'ram_util_str': str}
- v2 returns {'tpu_mxu': float, tpu_mxu_str': str, 'tpu_idle_time': float, 'tpu_idle_str': str, 'cpu_util': float, 'ram_util': float, 'ram_util_str': str}
# Example
'v1': {'tpu_mxu': 52.88895420451343, 'tpu_mem_per': 100.0, 'tpu_mem_used': 198.5, 'tpu_mem_str': '198.50GB/127.96GB', 'cpu_util': 0.9, 'ram_util': 54.5, 'ram_util_str': '49.43GB/96.00GB'}

'''
stats = monitor.current_stats
tpu_mxu = stats.get('tpu_mxu', '')


```

<p align="center">
    <br>
    <img src="docs/tpumonitor.png"/>
    <br>
<p>

## Notes

There are currently 2 versions of TPUBar, v1 and v2. They each use different API calls to get TPU metrics to avoid compatability issues.

v1 is meant for TPU Projects running on GCE and/or Using Tensorflow < 2. Additionally, v1 can be called on a remote system (like your PC) to query your TPU running on GCE without being directly connected. Not yet tested, but should also be used in Pytorch training as well.

v2 is meant for Colab and/or Tensorflow 2+, and uses tensorflow APIs, which require the system to be directly connected to the TPUs.

They both return different values in current_stats as of right now.


## Contributors

[@shawwn](https://github.com/shawwn)

## Acknowledgements

[Tensorflow Research Cloud](https://www.tensorflow.org/tfrc) for providing TPU Resources