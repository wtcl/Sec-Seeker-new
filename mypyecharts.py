from typing import Tuple, List, Union
from pyecharts.charts import Graph
from pyecharts import options as opts


class RelationshipGraph:
    def __init__(self, width: int = 1024, height: int = 768):
        """
        create the RelationshipGraph Class
        :param width: width of the graph
        :param height: height of the graph
        """
        # store the relationship info
        # reasons and results are in this format:
        #     tuple (Entity, Predicate)
        self.entity = []
        # store the relationship in this format:
        #     tuple (Reason(Entity, Predicate) , Result(Entity, Predicate))
        self.relationship = []
        self.node_weight = {}
        self.graph = Graph(init_opts=opts.InitOpts(
            width="{}px".format(width),
            height="{}px".format(height)
        ))
        self.node = []
        self.link = []

    def add(self, reason: Tuple[str, str], result: Tuple[str, str]) -> None:
        """
        adding new reason-result tuple to graph
        :param reason: reason
        :param result: result
        :return: None
        """
        if reason not in self.entity:
            self.entity.append(reason)
            self.node_weight[reason] = 40
        else:
            self.node_weight[reason] += 5
        if result not in self.entity:
            self.entity.append(result)
            self.node_weight[result] = 40
        else:
            self.node_weight[result] += 5
        self.relationship.append((reason, result))

    def add_list(self, relationships: Union[
        List[Tuple[Tuple[str, str], Tuple[str, str]]], None]) -> None:
        """
        adding a list of (reason, result) to graph
        :param relationships: list of (reason, result)
        :return: None
        """
        for relation in relationships:
            self.add(relation[0], relation[1])

    def render(self, repulsion: int = 1000):
        """
        rendering the picture
        :param repulsion: the repulsion of picture
        :return: None
        """
        sym = {ent: "circle" for ent in self.entity}
        in_degree = {ent: 0 for ent in self.entity}
        out_degree = {ent: 0 for ent in self.entity}
        # calc the degrees of graph to specify the shape nodes use
        for rea, res in self.relationship:
            in_degree[res] += 1
            out_degree[rea] += 1
        for ent in sym:
            if in_degree[ent] == 0 and out_degree[ent] != 0:
                sym[ent] = "roundRect"
            elif in_degree[ent] != 0 and out_degree[ent] == 0:
                sym[ent] = "diamond"
        for tup in self.entity:
            self.node.append(
                opts.GraphNode(
                    name=tup[0],
                    symbol_size=self.node_weight[tup],
                    symbol=sym[tup],
                )
            )
        for rea, res in self.relationship:
            self.link.append(
                opts.GraphLink(
                    source=rea[0],
                    target=res[0] + res[1],
                    value=rea[1] + "."
                )
            )
        self.graph.add(
            series_name="",
            nodes=self.node,
            links=self.link,
            is_draggable=True,
            repulsion=repulsion,
            edge_label=opts.LabelOpts(
                is_show=True,
                position="middle",
                formatter="{c}"
            ),
            edge_symbol=['circle', 'arrow']
        )

    def save(self, path: str = "render.html") -> None:
        """
        save the picture as HTML
        :param path: HTML path
        :return: None
        """
        self.graph.render(path)


from typing import Tuple, List, Union

from pyecharts.charts import Graph
from pyecharts import options as opts


class RelationshipGraph:
    def __init__(self, width: int = 1024, height: int = 768):
        """
        create the RelationshipGraph Class
        :param width: width of the graph
        :param height: height of the graph
        """
        # store the relationship info
        # reasons and results are in this format:
        #     tuple (Entity, Predicate)
        self.entity = []
        # store the relationship in this format:
        #     tuple (Reason(Entity, Predicate) , Result(Entity, Predicate))
        self.relationship = []
        self.node_weight = {}
        self.graph = Graph(init_opts=opts.InitOpts(
            width="{}px".format(width),
            height="{}px".format(height)
        ))
        self.node = []
        self.link = []

    def add(self, reason: Tuple[str, str], result: Tuple[str, str]) -> None:
        """
        adding new reason-result tuple to graph
        :param reason: reason
        :param result: result
        :return: None
        """
        if reason not in self.entity:
            self.entity.append(reason)
            self.node_weight[reason] = 40
        else:
            self.node_weight[reason] += 5
        if result not in self.entity:
            self.entity.append(result)
            self.node_weight[result] = 40
        else:
            self.node_weight[result] += 5
        self.relationship.append((reason, result))

    def add_list(self, relationships: Union[
        List[Tuple[Tuple[str, str], Tuple[str, str]]], None]) -> None:
        """
        adding a list of (reason, result) to graph
        :param relationships: list of (reason, result)
        :return: None
        """
        for relation in relationships:
            self.add(relation[0], relation[1])

    def render(self, repulsion: int = 1000):
        """
        rendering the picture
        :param repulsion: the repulsion of picture
        :return: None
        """
        sym = {ent: "circle" for ent in self.entity}
        in_degree = {ent: 0 for ent in self.entity}
        out_degree = {ent: 0 for ent in self.entity}
        # calc the degrees of graph to specify the shape nodes use
        for rea, res in self.relationship:
            in_degree[res] += 1
            out_degree[rea] += 1
        for ent in sym:
            if in_degree[ent] == 0 and out_degree[ent] != 0:
                sym[ent] = "roundRect"
            elif in_degree[ent] != 0 and out_degree[ent] == 0:
                sym[ent] = "diamond"
        for tup in self.entity:
            self.node.append(
                opts.GraphNode(
                    name=tup[0],
                    symbol_size=self.node_weight[tup],
                    symbol=sym[tup],
                )
            )
        for rea, res in self.relationship:
            self.link.append(
                opts.GraphLink(
                    source=rea[0],
                    target=res[0] + res[1],
                    value=rea[1] + "."
                )
            )
        self.graph.add(
            series_name="",
            nodes=self.node,
            links=self.link,
            is_draggable=True,
            repulsion=repulsion,
            edge_label=opts.LabelOpts(
                is_show=True,
                position="middle",
                formatter="{c}"
            ),
            edge_symbol=['circle', 'arrow']
        )

    def save(self, path: str = "render.html") -> None:
        """
        save the picture as HTML
        :param path: HTML path
        :return: None
        """
        self.graph.render(path)


pair1_rea1 = ("张三", "感染")
pair1_rea2 = ("李四", "感染")
pair1_res = ("赵五", "")
pair2_rea1 = ("汤六", "感染")
pair2_rea2 = ("久久", "感染")
pair2_res = ("小明", "")
pair3_rea1 = pair2_rea2
pair3_rea2 = pair1_rea1
pair3_res = ("丽丽", "")
pair4_res = ("二弟", "")
pair5_res = ("二个", "")
g = RelationshipGraph()
r = [(pair1_rea1, pair1_res), (pair1_rea2, pair1_res), (pair2_rea1, pair2_res),
     (pair2_rea2, pair2_res),
     (pair3_rea1, pair3_res), (pair3_rea2, pair3_res), (pair3_res, pair4_res),
     (pair5_res, pair5_res)]

g.add_list(r)
g.render()
g.save("./static/pycahrt/base.html")
