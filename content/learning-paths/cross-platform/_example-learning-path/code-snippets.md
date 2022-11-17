---
# User change
title: "How to add code snippets"

weight: 8 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

Explanation of this and that, talk about tips and this. Quick thing to do. Combine any of these (line number & highlighting display should be mutually exclusive).
Basic code entry
```
echo ‘hello world’
```

	Code highlighting based on language (list of supported languages)
```python
print(hello world)
```

	Line number display 		
```bash { line_numbers = “true” }
echo ‘hello world’
```

Line highlighting 		
```bash { highlight_lines = 5 }
echo ‘hello world’
```

```bash { highlight_lines = “1-2, 5, 9-20” }
echo ‘hello world’
```

Command line prompt, with optional output	 		
```bash { command_line=“root@localhost” }
echo ‘hello world’
```

```bash { command_line=“root@localhost | 2-5” }
echo ‘hello world’
```
