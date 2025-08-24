<jexpand>
prompt = "src/lib/track-state-changes.js"

for filename in prompt.split(" "):
    print(f"""file_xml("{filename}")""")
</jexpand>