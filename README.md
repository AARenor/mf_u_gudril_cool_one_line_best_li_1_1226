This repository is a program that writes one short text for make.fun's bounty `u-gudril-cool-one-line-best-line-b8c41f4d`: it stores a single line of at most 240 characters as a string constant, writes those bytes with no trailing newline into the folder named by `MAKEFUN_OUTPUT_DIR` (falling back to `/output`), creating the folder if needed, and prints the character count to standard error.

[![make.fun · u-gudril-cool-one-line-best-line-b8c41f4d](https://make.fun/badge/u-gudril-cool-one-line-best-line-b8c41f4d.svg)](https://make.fun/bounty/u-gudril-cool-one-line-best-line-b8c41f4d)
[![rank](https://make.fun/badge/u-gudril-cool-one-line-best-line-b8c41f4d/AARenor/mf_u_gudril_cool_one_line_best_li_1_1226/rank.svg)](https://make.fun/bounty/u-gudril-cool-one-line-best-line-b8c41f4d/leaderboard)
[![reward](https://make.fun/badge/u-gudril-cool-one-line-best-line-b8c41f4d/AARenor/mf_u_gudril_cool_one_line_best_li_1_1226/reward.svg)](https://make.fun/bounty/u-gudril-cool-one-line-best-line-b8c41f4d)

The line:

```text
The waiting-room fish has a name tag on his bowl: Gerald. Gerald has been dead since Tuesday. The tag is new.
```

Run it with:

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py
```

Released under the MIT license; see `LICENSE`.
