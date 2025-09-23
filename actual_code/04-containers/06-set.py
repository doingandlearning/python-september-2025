regions = ["NE", "SE", "London", "SE", "NI", "Cornwall", "Wales", "Scotland", "Scotland", "NI"]

regions = set(regions)
regions = list(regions)
regions.sort()

regions = list(set(regions))  # deduplicating the list

print(regions)