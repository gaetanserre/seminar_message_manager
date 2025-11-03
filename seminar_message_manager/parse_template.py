import pandas as pd


def parse_annoucement(date, seminar_csv, template):
    sem_data = pd.read_table(seminar_csv, sep=";", skipinitialspace=True)
    cur_sem = sem_data[sem_data.loc[:, "date"] == date]
    ext = template.split(".")[-1]
    template = open(template, "r").read()

    # Create the modified template
    for s in ["date", "first_name", "last_name"]:
        template = template.replace("{" + s + "}", str(cur_sem.loc[:, s].to_list()[0]))

    if pd.isna(cur_sem.loc[:, "work_link"].to_list()[0]):
        temp_rep = str(cur_sem.loc[:, "work_name"].to_list()[0])
    elif ext == "html":
        temp_rep = (
            "<a href='"
            + str(cur_sem.loc[:, "work_link"].to_list()[0])
            + "'>"
            + str(cur_sem.loc[:, "work_name"].to_list()[0])
            + "</a>"
        )
    else:
        temp_rep = (
            "["
            + str(cur_sem.loc[:, "work_name"].to_list()[0])
            + "]("
            + str(cur_sem.loc[:, "work_link"].to_list()[0])
            + ")"
        )
    template = template.replace("{work_name}", temp_rep)

    if pd.isna(cur_sem.loc[:, "location"].to_list()[0]):
        temp_rep = ""
    else:
        temp_rep = str(cur_sem.loc[:, "location"].to_list()[0])

    template = template.replace("{location}", temp_rep)
    return template
