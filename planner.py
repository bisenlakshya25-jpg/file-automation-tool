def check_duplicate(dest_folder, item, plans):
    base_name = item.stem
    extension = item.suffix
    counter = 0

    while True:
        if counter == 0:
            new_name = item.name
        else:
            new_name = f"{base_name}_{counter}{extension}"

        final_dest = dest_folder / new_name

        # Check filesystem + already planned destinations
        already_planned = any(
            planned_dest == final_dest
            for _, planned_dest in plans
        )

        if not final_dest.exists() and not already_planned:
            return final_dest

        counter += 1


def planner(organised_files, target_path):
    plans = []

    for item, category in organised_files:
        dest_folder = target_path / category

        final_dest = check_duplicate(
            dest_folder,
            item,
            plans
        )

        plans.append((item, final_dest))

    return plans
