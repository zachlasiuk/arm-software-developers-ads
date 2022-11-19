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

&nbsp;  

## Code Panes  


Adding a code pane, for code dependent on OS, architecture, or similar. Code panes are incompatible with the other forms of code styling.

Code pane example with language selector: (PROBLEM WITH NOT HAVING A SPACE HERE, LEADS TO ISSUES!!! IF TABPANE IS NEXT TO TEXT ABOVE IT WON'T WORK RIGHT.)

{{< tabpane code=true >}}
  {{< tab header="Python" lang="python">}}
print('hello world')
  {{< /tab >}}
  {{< tab header="Bash" lang="bash">}}
echo 'hello world'
  {{< /tab >}}
{{< /tabpane >}}

&nbsp;  

Example with line highlighting

{{< tabpane code=true >}}
  {{< tab header="Python" lang="python" highlight="2-3">}}
print('hello world')
print('higlight me')
print('and also me')
  {{< /tab >}}
  {{< tab header="Bash" lang="bash">}}
echo 'hello world'
echo 'highlight me'
echo 'not me'
echo 'but me'
  {{< /tab >}}
{{< /tabpane >}}

&nbsp;  


{{< tabpane code=true >}}
  {{< tab header="Ubuntu 22.04" >}}
sudo apt-get install jq minicom make cmake gdb-multiarch automake autoconf libtool libftdi-dev libusb-1.0-0-dev pkg-config clang-format -y
  {{< /tab >}}
  {{< tab header="Ubuntu 20.04" >}}
sudo apt-get install jq minicom make gdb-multiarch automake autoconf libtool libftdi-dev libusb-1.0-0-dev pkg-config clang-format -y
sudo snap install cmake --classic
  {{< /tab >}}
  {{< tab header="Raspberry Pi OS" >}}
Nothing more to install!
  {{< /tab >}}
{{< /tabpane >}}
