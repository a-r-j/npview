# NPView

CLI tools for quickly viewing data in various formats (eventually). Currently only `.npy` files are supported.

## Installation

```bash
pip install npview
```

## Usage

```bash
npv {PATH_TO_YOUR_FILE.npy} {THRESHOLD}
```

Where `{THRESHOLD}` is an integer specifying Total number of array elements which trigger summarization rather than full repr. Default is `sys.maxsize`.
