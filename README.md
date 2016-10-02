# Using Bokeh to Display Live Data

This is an example of using Bokeh to display live data on a website. While this data is randomly generated, it should be straightforward to apply it to data coming in from an external source.

## Instructions for Use

Download the [latest version of Miniconda](http://conda.pydata.org/miniconda.html) for your platform and install it. Issue the following command to install Bokeh and its dependencies.

```
$ conda install bokeh
```

To test the server locally, run

```
$ bokeh serve --show myapp.py
```

For deploying the app on a network, you need to configure the hostname and address for the server. Please refer to the Bokeh manual for how to do this.
