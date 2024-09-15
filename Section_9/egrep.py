import sys, re

# sys.argv[1]は，コマンドライン引数のリスト
# sys.argv[0]は，プログラム名
# sys.argc[1]は，コマンドライン上に指定した正規表現
regex = sys.argv[1]

# スクリプトが処理する各行に対して
for line in sys.stdin:
    # 正規表現に合致したなら，stdoutに出力する
    if re.search(regex, line):
        sys.stdout.write(line)