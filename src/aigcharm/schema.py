"""Dataset schema constants for AIGenHarm-Video."""

CATEGORIES = [
    "C1_Hate_Harassment_Threats",
    "C2_Violence_Dangerous_Acts",
    "C3_Sexual_Content_Nudity",
    "C4_Child_Safety",
    "C5_Illegal_Activities_Regulated_Goods",
    "C6_Misinformation_Political_Sensitivity",
]

REQUIRED_COLUMNS = [
    "video_id",
    "platform",
    "harmfulness",
    "presentation",
    *CATEGORIES,
]

DATASET_STATS = {
    "total": 1808,
    "harmful": 993,
    "safe": 815,
    "platforms": {
        "tiktok": {"total": 973, "harmful": 528, "safe": 445},
        "bilibili": {"total": 835, "harmful": 465, "safe": 370},
    },
    "presentation": {
        "explicit_harmful": 672,
        "implicit_harmful": 321,
    },
    "category_counts": {
        "C1": 178,
        "C2": 618,
        "C3": 354,
        "C4": 102,
        "C5": 423,
        "C6": 182,
    },
}
