from graphviz import Digraph


def create_er_diagram():
    # グラフの設定
    dot = Digraph(name="ER_Diagram", filename="er_diagram", format="png")
    dot.attr(rankdir="LR", splines="polyline")

    # =============================
    # テーブル: temporary_spots
    # =============================
    dot.node(
        "temporary_spots",
        label=(
            "<<TABLE BORDER='1' CELLBORDER='1' CELLSPACING='0' CELLPADDING='4'>"
            "<TR><TD BGCOLOR='lightblue' COLSPAN='2'><B>temporary_spots</B></TD></TR>"
            "<TR><TD><I>id</I></TD><TD>UUID (PK)</TD></TR>"
            "<TR><TD>title</TD><TD>TEXT NOT NULL</TD></TR>"
            "<TR><TD>slug</TD><TD>TEXT NOT NULL UNIQUE</TD></TR>"
            "<TR><TD>nearest_station</TD><TD>TEXT</TD></TR>"
            "<TR><TD>opening_hours</TD><TD>TEXT</TD></TR>"
            "<TR><TD>image</TD><TD>JSONB</TD></TR>"
            "<TR><TD>description</TD><TD>TEXT NOT NULL</TD></TR>"
            "<TR><TD>category_id</TD><TD>UUID (FK)</TD></TR>"
            "<TR><TD>address_lat</TD><TD>NUMERIC NOT NULL</TD></TR>"
            "<TR><TD>address_lng</TD><TD>NUMERIC NOT NULL</TD></TR>"
            "<TR><TD>meta</TD><TD>JSONB</TD></TR>"
            "<TR><TD>start_date</TD><TD>TIMESTAMP WITH TIME ZONE NOT NULL</TD></TR>"
            "<TR><TD>end_date</TD><TD>TIMESTAMP WITH TIME ZONE NOT NULL</TD></TR>"
            "<TR><TD>status</TD><TD>spot_status NOT NULL DEFAULT 'draft'</TD></TR>"
            "<TR><TD>created_at</TD><TD>TIMESTAMP WITH TIME ZONE DEFAULT now()</TD></TR>"
            "<TR><TD>updated_at</TD><TD>TIMESTAMP WITH TIME ZONE DEFAULT now()</TD></TR>"
            "</TABLE>>"
        ),
        shape="none",
    )

    # =============================
    # テーブル: categories
    # =============================
    dot.node(
        "categories",
        label=(
            "<<TABLE BORDER='1' CELLBORDER='1' CELLSPACING='0' CELLPADDING='4'>"
            "<TR><TD BGCOLOR='lightblue' COLSPAN='2'><B>categories</B></TD></TR>"
            "<TR><TD><I>id</I></TD><TD>UUID (PK)</TD></TR>"
            "<TR><TD>name</TD><TD>TEXT NOT NULL</TD></TR>"
            "<TR><TD>slug</TD><TD>TEXT NOT NULL UNIQUE</TD></TR>"
            "<TR><TD>created_at</TD><TD>TIMESTAMP WITH TIME ZONE DEFAULT now()</TD></TR>"
            "<TR><TD>updated_at</TD><TD>TIMESTAMP WITH TIME ZONE DEFAULT now()</TD></TR>"
            "</TABLE>>"
        ),
        shape="none",
    )

    # =============================
    # テーブル: tags
    # =============================
    dot.node(
        "tags",
        label=(
            "<<TABLE BORDER='1' CELLBORDER='1' CELLSPACING='0' CELLPADDING='4'>"
            "<TR><TD BGCOLOR='lightblue' COLSPAN='2'><B>tags</B></TD></TR>"
            "<TR><TD><I>id</I></TD><TD>UUID (PK)</TD></TR>"
            "<TR><TD>name</TD><TD>TEXT NOT NULL</TD></TR>"
            "<TR><TD>slug</TD><TD>TEXT NOT NULL UNIQUE</TD></TR>"
            "<TR><TD>created_at</TD><TD>TIMESTAMP WITH TIME ZONE DEFAULT now()</TD></TR>"
            "<TR><TD>updated_at</TD><TD>TIMESTAMP WITH TIME ZONE DEFAULT now()</TD></TR>"
            "</TABLE>>"
        ),
        shape="none",
    )

    # =============================
    # テーブル: temporary_spot_tags
    # =============================
    dot.node(
        "temporary_spot_tags",
        label=(
            "<<TABLE BORDER='1' CELLBORDER='1' CELLSPACING='0' CELLPADDING='4'>"
            "<TR><TD BGCOLOR='lightblue' COLSPAN='2'><B>temporary_spot_tags</B></TD></TR>"
            "<TR><TD><I>(PK)</I></TD><TD>temporary_spot_id + tag_id</TD></TR>"
            "<TR><TD>temporary_spot_id</TD><TD>UUID (FK)</TD></TR>"
            "<TR><TD>tag_id</TD><TD>UUID (FK)</TD></TR>"
            "<TR><TD>created_at</TD><TD>TIMESTAMP WITH TIME ZONE DEFAULT now()</TD></TR>"
            "</TABLE>>"
        ),
        shape="none",
    )

    # =============================
    # テーブル: votes
    # =============================
    dot.node(
        "votes",
        label=(
            "<<TABLE BORDER='1' CELLBORDER='1' CELLSPACING='0' CELLPADDING='4'>"
            "<TR><TD BGCOLOR='lightblue' COLSPAN='2'><B>votes</B></TD></TR>"
            "<TR><TD><I>id</I></TD><TD>UUID (PK)</TD></TR>"
            "<TR><TD>temporary_spot_id</TD><TD>UUID (FK)</TD></TR>"
            "<TR><TD>user_id</TD><TD>UUID</TD></TR>"
            "<TR><TD>ip_address</TD><TD>INET</TD></TR>"
            "<TR><TD>created_at</TD><TD>TIMESTAMP WITH TIME ZONE DEFAULT now()</TD></TR>"
            "</TABLE>>"
        ),
        shape="none",
    )

    # =============================
    # テーブル: newsletter_issues
    # =============================
    dot.node(
        "newsletter_issues",
        label=(
            "<<TABLE BORDER='1' CELLBORDER='1' CELLSPACING='0' CELLPADDING='4'>"
            "<TR><TD BGCOLOR='lightblue' COLSPAN='2'><B>newsletter_issues</B></TD></TR>"
            "<TR><TD><I>id</I></TD><TD>UUID (PK)</TD></TR>"
            "<TR><TD>subject</TD><TD>TEXT NOT NULL</TD></TR>"
            "<TR><TD>content</TD><TD>TEXT NOT NULL</TD></TR>"
            "<TR><TD>sent_at</TD><TD>TIMESTAMP WITH TIME ZONE</TD></TR>"
            "</TABLE>>"
        ),
        shape="none",
    )

    # =============================
    # テーブル: newsletter_subscribers
    # =============================
    dot.node(
        "newsletter_subscribers",
        label=(
            "<<TABLE BORDER='1' CELLBORDER='1' CELLSPACING='0' CELLPADDING='4'>"
            "<TR><TD BGCOLOR='lightblue' COLSPAN='2'><B>newsletter_subscribers</B></TD></TR>"
            "<TR><TD><I>id</I></TD><TD>UUID (PK)</TD></TR>"
            "<TR><TD>email</TD><TD>TEXT NOT NULL UNIQUE</TD></TR>"
            "<TR><TD>subscribed_at</TD><TD>TIMESTAMP WITH TIME ZONE DEFAULT now()</TD></TR>"
            "</TABLE>>"
        ),
        shape="none",
    )

    # =============================
    # テーブル: newsletter_sends
    # =============================
    dot.node(
        "newsletter_sends",
        label=(
            "<<TABLE BORDER='1' CELLBORDER='1' CELLSPACING='0' CELLPADDING='4'>"
            "<TR><TD BGCOLOR='lightblue' COLSPAN='2'><B>newsletter_sends</B></TD></TR>"
            "<TR><TD><I>id</I></TD><TD>UUID (PK)</TD></TR>"
            "<TR><TD>newsletter_issue_id</TD><TD>UUID (FK)</TD></TR>"
            "<TR><TD>subscriber_id</TD><TD>UUID (FK)</TD></TR>"
            "<TR><TD>sent_at</TD><TD>TIMESTAMP WITH TIME ZONE DEFAULT now()</TD></TR>"
            "</TABLE>>"
        ),
        shape="none",
    )

    # =============================
    # spot_status（列挙型）
    # =============================
    # ENUM 型はテーブルではないですが、必要に応じて図示するなら以下のような形でノードを作ってもOKです。
    # 今回は列挙型のため、簡単にノードのみ追加例を示します。
    dot.node(
        "spot_status",
        label=(
            "<<TABLE BORDER='1' CELLBORDER='1' CELLSPACING='0' CELLPADDING='4'>"
            "<TR><TD BGCOLOR='lightgreen'><B>spot_status</B></TD></TR>"
            "<TR><TD>'draft'</TD></TR>"
            "<TR><TD>'published'</TD></TR>"
            "<TR><TD>'deleted'</TD></TR>"
            "</TABLE>>"
        ),
        shape="none",
    )

    # =============================
    # 外部キー(FK)のリレーション
    # =============================

    # temporary_spots -> categories (category_id)
    dot.edge("temporary_spots", "categories", label="category_id → id")

    # votes -> temporary_spots (temporary_spot_id)
    dot.edge("votes", "temporary_spots", label="temporary_spot_id → id")

    # temporary_spot_tags -> temporary_spots (temporary_spot_id)
    dot.edge("temporary_spot_tags", "temporary_spots", label="temporary_spot_id → id")

    # temporary_spot_tags -> tags (tag_id)
    dot.edge("temporary_spot_tags", "tags", label="tag_id → id")

    # newsletter_sends -> newsletter_issues (newsletter_issue_id)
    dot.edge("newsletter_sends", "newsletter_issues", label="newsletter_issue_id → id")

    # newsletter_sends -> newsletter_subscribers (subscriber_id)
    dot.edge("newsletter_sends", "newsletter_subscribers", label="subscriber_id → id")

    # temporary_spots.status -> spot_status
    dot.edge("temporary_spots", "spot_status", label="status → spot_status (ENUM)")

    # ER 図の描画 (er_diagram.png が生成される)
    output_path = "./Supabase"
    dot.render(output_path, cleanup=True)


if __name__ == "__main__":
    create_er_diagram()
