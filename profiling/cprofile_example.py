import cProfile

"""
python -m cProfile -o log.pstats <binary_file>
python -m cProfile -o log.pstats -m <module>
python -m cProfile -o log.pstats <script>

python -m pstats log.pstats
sort cumtime
stats 10
"""

"""
graph to view the stats
pip install yelp-gprof2dot
grof2dot log.pstats | dot -Tsvg -o log.svg
"""


def main() -> None:
    cProfile.run("[x for x in range(1500)]")


if __name__ == "__main__":
    main()
