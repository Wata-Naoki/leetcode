from pprint import pprint

points = ["淵野辺駅北口", "5叉路", "理容モダン", "幸町児童館", "ファミマ",  "グランメール",
          "ZeroMax",  "JA相模原",  "調剤薬局",  "つきあたり",  "ボニータ",  "淵野辺入口",
          "ドミノピザ",  "信号",  "曲がり角",  "アゼリア",  "三叉路",  "青学大正門"]
routes = {
    ((points[0], points[1]), 134),  ((points[0], points[4]), 167),  # 淵野辺駅北口から
    ((points[1], points[2]), 114),  ((points[1], points[6]), 171),  # 5叉路から
    ((points[2], points[3]), 126),  ((points[2], points[7]), 166),  # 理容モダンから
    ((points[3], points[8]), 178),  # 幸町児童館から
    ((points[4], points[5]), 64),   ((points[4], points[9]), 135),  # ファミマから
    ((points[5], points[6]), 61),   ((points[5], points[10]), 137),  # グランメールから
    ((points[6], points[7]), 70),   ((
        points[6], points[11]), 165),  # ZeroMaxから
    ((points[7], points[8]), 104),  ((points[7], points[13]), 276),  # JA相模原から
    ((points[8], points[13]), 194),  # 調剤薬局から
    ((points[9], points[10]), 58),  # つきあたりから
    ((points[10], points[11]), 57),  # ボニータから
    ((points[11], points[12]), 73), ((points[11], points[16]), 199),  # 淵野辺入口から
    ((points[12], points[13]), 71), ((points[12], points[14]), 45),  # ドミノピザから
    ((points[13], points[15]), 50),  # 信号から
    ((points[14], points[15]), 89),  # 曲がり角から
    ((points[15], points[17]), 104),  # アゼリアから
    ((points[16], points[17]), 108)  # 三叉路から
}

# pprint(routes)

# ひとつ前の地点と、そこまでの距離を求めるデータ構造にする。


def get_reverse_graph(routes):
    a_graph = {}
    for route in routes:
        from_v = route[0][0]
        to_v = route[0][1]
        dist = route[1]
        if not to_v in a_graph:
            a_graph[to_v] = []
        a_graph[to_v].append((from_v, dist))
    return a_graph


a_graph = get_reverse_graph(routes)
# pprint(a_graph)


def get_min_path(graph, start_p, end_p):
    # 関数の引数から、決定済みの辞書と、未決定の集合を作成
    determined = {start_p: 0}
    undetermined = set(graph.keys())

    # 終点の最短距離が未決定のうちはループ
    while not end_p in determined:

        # 未決定の地点ごとにループ
        for point in undetermined:

            min_dist = None
            for from_p, dist in graph[point]:
                if from_p in determined:
                    if min_dist == None:
                        min_dist = determined[from_p] + dist
                    else:
                        min_dist = min(min_dist, determined[from_p] + dist)
            if not min_dist == None:
                determined[point] = min_dist

    return determined[end_p]


# プログラムを動かしてみる。
start_point = "淵野辺駅北口"
end_point = "青学大正門"
print(
    f"shortest path from {start_point} to {end_point} is {get_min_path(a_graph, start_point, end_point)}")
