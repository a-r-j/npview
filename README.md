# NPView

[![PyPI version](https://badge.fury.io/py/npview.svg)](https://badge.fury.io/py/npview)
![supported python versions](https://img.shields.io/pypi/pyversions/npview)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

CLI tools for quickly viewing data in various formats (eventually). Currently only `.npy` and `.csv`/`.tsv` files are supported.

## Installation

```bash
pip install npview
```

## Usage

### CSV

Results in a nicely-formatted and interactive view of the csv data with sidescrolling. Quit by pressing `q`. The number of rows and columsnare printed on exit.

```bash
csv {PATH_TO_YOUR_FILE.csv}
```

```bash
      1 Unnamed: 0  PDB  chain  sequence  interacting_residues                                                                                                                                   >
      2 181         181  5h9i   A         GPHMTGLAAISDALAADLAGLSFSSPVAHVYNPLLYAREPHVAYLSRFGSPPKEVLFVGMNPGPWGMAQTGVPFGEVAVVTEWLGINGTVTRPAGEHPKKRVDGFACRRSEVSGRRLWGFIRERFGTPERFFARFFVANYCPLLFLTAEGG>
      3 19          19   1jdw   A         CPVSSYNEWDPLEEVIVGRAENACVPPFTIEVKANTYEKYWPFYQKQGGHYFPKDHLKKAVAEIEEMCNILKTEGVTVRRPDPIDWSLKYKTPDFESTGLYSAMPRDILIVVGNEIIEAPMAWRSRFFEYRAYRSIIKDYFHRGAKWTTAP>
      4 91          91   2irp   A         NVELFKKFSEKVEEIIEAGRILHSRGWVPATSGNISAKVSEEYIAITASGKHKGKLTPEDILLIDYEGRPVGGGKPSAETLLHTTVYKLFPEVNAVVHTHSPNATVISIVEKKDFVELEDYELLKAFPDIHTHEVKIKIPIFPNEQNIPLL>
      5 28          28   1m8z   A         GRSRLLEDFRNNRYPNLQLREIAGHIMEFSQDQHGSRFIQLKLERATPAERQLVFNEILQAAYQLMVDVFGNYVIQKFFEFGSLEQKLALAERIRGHVLSLALQMYGCRVIQKALEFIPSDQQNEMVRELDGHVLKCVKDQNGNHVVQKCI>
      6 97          97   2jpt   A         GSELETAMETLINVFHAHSGKEGDKYKLSKKELKELLQTELSGFLDAQKDADAVDKVMKELDEDGDGEVDFQEYVVLVAALTVACNNFFWENS                                                          >
      7 125         125  3ew8   A         LVPVYIYSPEYVSMCDSLAKIPKRASMVHSLIEAYALHKQMRIVKPKVASMEEMATFHTDAYLQHLQKVSQEGEYGLGYLCPATEGIFDYAAAIGGATITAAQCLIDGMCKVAINWSGGWHHAKKDEASGFCYLNDAVLGILRLRRKFERI>
      8 152         152  3sjz   A         AWPKVQPEVNIGVVGHVDHGKTTLVQAITGIWTSKHSEETIKLGYAETNIGVCESCKKPEAYVTEPSCKSCGSDDEPKFLRRISFIDAPGHEVLMATMLSGAALMDGAILVVAANEPFPQPQTREHFVALGIIGVKNLIIVQNKVDVVSKE>
      9 161         161  4ehs   A         SAPSLEFLEKLVIRYLLEDRSLLDLAVGYIHSGVFLHKKQEFDALCQEKLDDPKLVALLLDANLPLKKGGFEKELRLLILRYFERQLKEIPKSSLPFSEKXICLKKARQAIXKLKQGELVAILE                           >
     10 115         115  3bit   A         XEELNIDFDVFKKRIELLYSKYNEFEGSPNSLLFVLGSSNAENPYQKTTILHNWLLSYEFPATLIALVPGKVIIITSSAKAKHLQKAIDLFKDPESKITLELWQRNNKEPELNKKLFDDVIALINSAGKTVGIPEKDSYQGKFXTEWNPVW>
     11 164         164  4iu4   A         KKMSIVLAPFSGGQPHSGVELGPDYLLKQGLQQDMEKLGWDTRLERVFDGKVVEARKASDNGDRIGRVKRPRLTAECTEKIYKCVRRVAEQGRFPLTIGGDHSIALGTVAGVLSVHPDAGVIWVDAHADINTMSGTVSGNLHGCPLSILLG>

Num Rows: 
11 test.csv
Num Columns: 
8

```

```bash
npp {PATH_TO_YOUR_FILE.npy}
```

### NumPY

```bash
npv {PATH_TO_YOUR_FILE.npy} {THRESHOLD}
```

Where `{THRESHOLD}` is an integer specifying Total number of array elements which trigger summarization rather than full repr. Default is `sys.maxsize`.

```bash
npp {PATH_TO_YOUR_FILE.npy}
```

Will attempt to print your saved matrix & itss dimensions using [prettymatrix](https://github.com/samueljamesbell/prettymatrix):

```bash
(2x2)
 ┌          ┐
 │ 1   22   │
 │ 333 4444 │
 └          ┘
```
