from graphviz import Digraph


def create_er_diagram(output_path="./Newt-CMS"):
    dot = Digraph("ERDiagram")
    dot.attr(rankdir="LR")

    # ------------------------------------------------------------------------
    # limited_time_article ノード
    # ------------------------------------------------------------------------
    dot.node(
        "limited_time_article",
        """<<TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0">
        <TR><TD COLSPAN="2"><B>limited_time_article</B></TD></TR>
        <TR><TD ALIGN="LEFT">title</TD><TD>String (Required, Unique, Title)</TD></TR>
        <TR><TD ALIGN="LEFT">slug</TD><TD>String (Required, Unique)</TD></TR>
        <TR><TD ALIGN="LEFT">author</TD><TD>Reference: Author (Required)</TD></TR>
        <TR><TD ALIGN="LEFT">image</TD><TD>Image (Optional)</TD></TR>
        <TR><TD ALIGN="LEFT">body</TD><TD>String (Required)</TD></TR>
        <TR><TD ALIGN="LEFT">tags</TD><TD>Reference: Tag[] (Required, Multiple)</TD></TR>
        <TR><TD ALIGN="LEFT">category</TD><TD>Reference: Category (Required)</TD></TR>
        <TR><TD ALIGN="LEFT">address</TD><TD>Address (Required)</TD></TR>
        <TR><TD ALIGN="LEFT">start_day</TD><TD>Date/Datetime (Required)</TD></TR>
        <TR><TD ALIGN="LEFT">end_day</TD><TD>Date/Datetime (Required)</TD></TR>
        <TR><TD ALIGN="LEFT">nearest_station</TD><TD>String (Required)</TD></TR>
        <TR><TD ALIGN="LEFT">opening_hours</TD><TD>Time Only (Optional)</TD></TR>
        <TR><TD ALIGN="LEFT">closing_hours</TD><TD>Time Only (Optional)</TD></TR>
        <TR><TD ALIGN="LEFT">meta</TD><TD>Custom Type (Optional)
            <BR/>- title
            <BR/>- details
            <BR/>- ogimage</TD></TR>
        </TABLE>>""",
        shape="plaintext",
    )

    # ------------------------------------------------------------------------
    # always_free_article ノード
    # ------------------------------------------------------------------------
    dot.node(
        "always_free_article",
        """<<TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0">
        <TR><TD COLSPAN="2"><B>always_free_article</B></TD></TR>
        <TR><TD ALIGN="LEFT">title</TD><TD>String (Required, Unique, Title)</TD></TR>
        <TR><TD ALIGN="LEFT">slug</TD><TD>String (Required, Unique)</TD></TR>
        <TR><TD ALIGN="LEFT">author</TD><TD>Reference: Author (Required)</TD></TR>
        <TR><TD ALIGN="LEFT">image</TD><TD>Image (Optional)</TD></TR>
        <TR><TD ALIGN="LEFT">body</TD><TD>String (Required)</TD></TR>
        <TR><TD ALIGN="LEFT">nearest_station</TD><TD>String (Required)</TD></TR>
        <TR><TD ALIGN="LEFT">opening_hours</TD><TD>Time Only (Optional)</TD></TR>
        <TR><TD ALIGN="LEFT">closing_hours</TD><TD>Time Only (Optional)</TD></TR>
        <TR><TD ALIGN="LEFT">category</TD><TD>Reference: Category (Required)</TD></TR>
        <TR><TD ALIGN="LEFT">tags</TD><TD>Reference: Tag[] (Required, Multiple)</TD></TR>
        <TR><TD ALIGN="LEFT">address</TD><TD>Address (Required)</TD></TR>
        <TR><TD ALIGN="LEFT">meta</TD><TD>Custom Type (Optional)
            <BR/>- title
            <BR/>- details
            <BR/>- ogimage</TD></TR>
        </TABLE>>""",
        shape="plaintext",
    )

    # ------------------------------------------------------------------------
    # author ノード
    # ------------------------------------------------------------------------
    dot.node(
        "author",
        """<<TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0">
        <TR><TD COLSPAN="2"><B>author</B></TD></TR>
        <TR><TD ALIGN="LEFT">fullName</TD><TD>String (Required, Title)</TD></TR>
        <TR><TD ALIGN="LEFT">slug</TD><TD>String (Required, Unique)</TD></TR>
        <TR><TD ALIGN="LEFT">biography</TD><TD>String (Required)</TD></TR>
        <TR><TD ALIGN="LEFT">profileImage</TD><TD>Image (Optional)</TD></TR>
        </TABLE>>""",
        shape="plaintext",
    )

    # ------------------------------------------------------------------------
    # tag ノード
    # ------------------------------------------------------------------------
    dot.node(
        "tag",
        """<<TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0">
        <TR><TD COLSPAN="2"><B>tag</B></TD></TR>
        <TR><TD ALIGN="LEFT">name</TD><TD>String (Required, Unique, Title)</TD></TR>
        <TR><TD ALIGN="LEFT">slug</TD><TD>String (Required, Unique)</TD></TR>
        </TABLE>>""",
        shape="plaintext",
    )

    # ------------------------------------------------------------------------
    # category ノード
    # ------------------------------------------------------------------------
    dot.node(
        "category",
        """<<TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0">
        <TR><TD COLSPAN="2"><B>category</B></TD></TR>
        <TR><TD ALIGN="LEFT">name</TD><TD>String (Required, Unique, Title)</TD></TR>
        <TR><TD ALIGN="LEFT">slug</TD><TD>String (Required, Unique)</TD></TR>
        </TABLE>>""",
        shape="plaintext",
    )

    # ------------------------------------------------------------------------
    # リレーション (limited_time_article)
    # 例のデザインに合わせ、「1-to-1」「1-to-many」などをシンプルに表記
    # ------------------------------------------------------------------------
    dot.edge("limited_time_article", "author", label="1-to-1")
    dot.edge("limited_time_article", "category", label="1-to-1")
    dot.edge("limited_time_article", "tag", label="1-to-many")

    # ------------------------------------------------------------------------
    # リレーション (always_free_article)
    # ------------------------------------------------------------------------
    dot.edge("always_free_article", "author", label="1-to-1")
    dot.edge("always_free_article", "category", label="1-to-1")
    dot.edge("always_free_article", "tag", label="1-to-many")

    # ------------------------------------------------------------------------
    # ER図出力 (PNGファイルなど)
    # ------------------------------------------------------------------------
    dot.render(output_path, format="png", cleanup=True)
    return dot


if __name__ == "__main__":
    create_er_diagram()
