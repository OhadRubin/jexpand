<jexpand>
prompt = "src/lib/track-state-changes.js src/lib/orchestration/protocol-imports.js"

for filename in prompt.split(" "):
    print(f'file_xml("/Users/ohadr/Auto-Craft-Bot/{filename}")')
</jexpand>