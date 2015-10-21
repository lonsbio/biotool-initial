# biotool (WIP)

Template bioinformatics script in various languages based on "Ten recommendations for creating usable bioinformatics command line software" by [Torsten Seemann.](https://twitter.com/torstenseemann)

- http://www.gigasciencejournal.com/content/2/1/15

This stuff should be easy; it is the actual bioinformatics that is hard.


# Torsten's Rules

1. Print something if no parameters are supplied
2. Always have a “-h” or “--help” switch
3. Have a “-v” or “--version” switch
4. Do not use stdout for messages and errors
5. Always raise an error if something goes wrong
6. Validate your parameters
7. Don’t hard-code any paths
8. Don’t pollute the PATH
9. Check that your dependencies are installed
-  Don’t distribute bare JAR files

# Extra Rules in progress (in order of making them up!)
> 11: Log early, log often

The road to hell is paved with diagnostic print statements. Logging of informative, warning and error messages really should occur, even if it's only during development or debugging, so begin with simple logging in your template.

A common approach is take have levels that are easy to use, and the location of output files customisable. -v, -vv, -vvv for various levels of verbosity. -q for quiet

> 12: It's only temporary

Temporary files should go somewhere sensible, but can be customised. They might be vary large, or very small, and there could be a reason to locate them somewhere specific.

> 13: (If it makes sense) read from STDIN, write to STDOUT by default

Build your tool with pipelines in mind. An output file can be desirable in many, but not all situations.

```bash
biotool_a < input.fasta  | biotool_b | biotool_c > output.fasta
```

If output files are likely, make it an optional and customisable

```bash
biotool --output output.results input.fasta
```

> 14:

.....


> 15: Make it easy to cite

Software can often be forgotten in the citation list. Remind your users. Tools for bioinformatics should be cited.  We've added --citation and --doi to make tools truly citable and citation information accesible directly from the command line.
For example, we could add:

```bash
biotool --citation
```
which returns

```text
Seemann, T. (2013). Ten recommendations for creating usable bioinformatics
command line software. GigaScience, 2, 15. doi:10.1186/2047-217X-2-15
```
and

```bash
biotool --doi
```
which returns

```text
biotool doi:10.1186/2047-217X-2-15
```

If your tool is code only, you could use a service such as Zenodo to create the DOI. https://guides.github.com/activities/citable-code/

In this way even if the source moves later on, the --doi link should be able to redirect to where the code is hosted.

> 15: Dependencies

shutil.which("python")
https://docs.python.org/dev/library/shutil.html

for non python programs.

For python modules?

> 16: Don't forget about memory

For Java....

> 17: Give detailed information when required

Logs should be useful and readable; what's in them can depend on whether they are working or not! Provide options to increase or decrease messages in logs.

|argument|value|comment|
|:--|:--|:--|
|--debug|     loglevel=logging.DEBUG|
|--verbose|  loglevel=logging.INFO|
| --quiet | loglevel=logging.ERROR | i.e suppress WARNING, but ERROR/CRITICAL messages will come through|
|default|   loglevel=logging.WARNING|


## Implementations


#### *Caveats*


Handling of command line options elegantly in various languages can come down to personal preference of existing options parsing libraries; If your favourite isn't listed, branches with alternate libraries are welcome.

### Python
**Status: template**



  This is actually tricky given the choice to use sub commands (see 8.) and argparser, but is n't impossible.

2. Always have a “-h” or “--help” switch

  Argparser gives this for free.

3. Have a “-v” or “--version” switch

  We add this with argparse (though note we'll use the -v shortcut for somthing else)
  ```python
    somethuihg.add('-v',"--version")
  ```

  8. Don’t pollute the PATH
    1. Use only one master command, which is used to invoke sub-commands. This is used effectively by popular software like SAMtools[7].
    2. Prefix all your sub-tools and helper scripts with the name biotool-.
    3. Ensure internal helper scripts are non-executable, so they don’t get indexed in the PATH, and instead invoke the scripts explicitly from biotool.
    4. Place them in a separate sub-folder (eg., auxiliary/, scripts/) and explicitly call them (but take note of rule #7 above).





### Java
**Status: skeleton**

Rule 10, "Don’t distribute bare JAR files", is translated verbatim from the rules in the executable `biotool_jar.sh`:

```bash
#!/bin/bash
java -Xmx512m -jar $(dirname $0)/BioTool.jar $*
```

The other principles of the rules for well behaved command line tools implemented in Java will be in `BioTool.java`, which has been packaged into `BioTool.jar`. `biotool_jar.sh` and `BioTool.jar` are in the same directory as the shell script implies, and the first executes the second.

Currently, only placeholder code exists.

`BioTool.java`:
```java

public class BioTool{

  public static void main(String[] args) {

    System.out.println("# BioTool");

    /* Insert bioinformatics here!*/

  }

}

```
