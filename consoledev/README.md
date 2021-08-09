<h1>Documentation: Version 1.0.0</h1>
<h3>Installation</h3>
You can install the module from pypi's website, or 
directly via the pip manager: <br/>
<code>pip install consoledev</code>
<br/>
<h3>Should I install?</h3>
If you want to make a pretty and basic console project, without 
spending the extra time to do this the right way, and eventually end up
with a messy project, then this module is for you. <br/>

<h3>Examples of usages:</h3>
First, you need to import consolekit:
<code> from consoledev import consolekit</code>
<h5>Example 1 - Basic Python Console:</h5>
<pre>
header = Text("BASIC PYTHON CONSOLE V1.0 ", COLORS.WARNING)
python_console = JConsole(header=header, starting_message="hello and welcome !", ending_message=" goodbye !")
python_console.run()
</pre>