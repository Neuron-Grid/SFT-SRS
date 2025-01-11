from graphviz import Digraph

# ER図生成
dot = Digraph("ERDiagram")

# Spotモデル
dot.node(
    "Spot",
    """<<TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0">
    <TR><TD COLSPAN="2"><B>Spot</B></TD></TR>
    <TR><TD ALIGN="LEFT">title</TD><TD>String (Unique, Required)</TD></TR>
    <TR><TD ALIGN="LEFT">slug</TD><TD>String (Unique, Required)</TD></TR>
    <TR><TD ALIGN="LEFT">nearest_station</TD><TD>String (Optional)</TD></TR>
    <TR><TD ALIGN="LEFT">opening_hours</TD><TD>String (Optional)</TD></TR>
    <TR><TD ALIGN="LEFT">image</TD><TD>Image (Custom Type)</TD></TR>
    <TR><TD ALIGN="LEFT">description</TD><TD>String (Required, Markdown)</TD></TR>
    <TR><TD ALIGN="LEFT">category</TD><TD>Category (Required, Reference)</TD></TR>
    <TR><TD ALIGN="LEFT">tags</TD><TD>Tag[] (Required, Multiple)</TD></TR>
    <TR><TD ALIGN="LEFT">meta</TD><TD>Meta (Custom Type)</TD></TR>
    <TR><TD ALIGN="LEFT">address</TD><TD>Address (Custom Type)</TD></TR>
</TABLE>>""",
    shape="plaintext",
)

# Categoryモデル
dot.node(
    "Category",
    """<<TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0">
    <TR><TD COLSPAN="2"><B>Category</B></TD></TR>
    <TR><TD ALIGN="LEFT">name</TD><TD>String (Required)</TD></TR>
    <TR><TD ALIGN="LEFT">slug</TD><TD>String (Unique, Required)</TD></TR>
</TABLE>>""",
    shape="plaintext",
)

# Tagモデル
dot.node(
    "Tag",
    """<<TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0">
    <TR><TD COLSPAN="2"><B>Tag</B></TD></TR>
    <TR><TD ALIGN="LEFT">name</TD><TD>String (Required)</TD></TR>
    <TR><TD ALIGN="LEFT">slug</TD><TD>String (Unique, Required)</TD></TR>
</TABLE>>""",
    shape="plaintext",
)

# 関連
dot.edge("Spot", "Category", label="1-to-1")
dot.edge("Spot", "Tag", label="1-to-many")

# ER図を出力
output_path = "./Newt-CMS"
dot.render(output_path, format="png", cleanup=True)
