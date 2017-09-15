# coding: utf-8

import os
import re

import pkg_resources


def __image_resource(filename):
    return pkg_resources.resource_filename(
        "cellprofiler",
        os.path.join("data", "images", filename)
    )


def read_content(filename):
    resource_filename = pkg_resources.resource_filename(
        "cellprofiler",
        os.path.join("data", "help", filename)
    )

    with open(resource_filename, "r") as f:
        content = f.read()

    return re.sub(
        r"image:: (.*\.png)",
        lambda md: "image:: {}".format(
            __image_resource(os.path.basename(md.group(0)))
        ),
        content
    )

X_AUTOMATIC_EXTRACTION = "Extract from image file headers"
X_MANUAL_EXTRACTION = "Extract from file/folder names"
X_IMPORTED_EXTRACTION = "Import from file"
VIEW_OUTPUT_SETTINGS_BUTTON_NAME = "View output settings"


####################
#
# ICONS
#
####################
MODULE_HELP_BUTTON = __image_resource('module_help.png')
MODULE_MOVEUP_BUTTON = __image_resource('module_moveup.png')
MODULE_MOVEDOWN_BUTTON = __image_resource('module_movedown.png')
MODULE_ADD_BUTTON = __image_resource('module_add.png')
MODULE_REMOVE_BUTTON = __image_resource('module_remove.png')
TESTMODE_PAUSE_ICON = __image_resource('IMG_PAUSE.png')
TESTMODE_GO_ICON = __image_resource('IMG_GO.png')
DISPLAYMODE_SHOW_ICON = __image_resource('eye-open.png')
DISPLAYMODE_HIDE_ICON = __image_resource('eye-close.png')
SETTINGS_OK_ICON = __image_resource('check.png')
SETTINGS_ERROR_ICON = __image_resource('remove-sign.png')
SETTINGS_WARNING_ICON = __image_resource('IMG_WARN.png')
RUNSTATUS_PAUSE_BUTTON = __image_resource('status_pause.png')
RUNSTATUS_STOP_BUTTON = __image_resource('status_stop.png')
RUNSTATUS_SAVE_BUTTON = __image_resource('status_save.png')
WINDOW_HOME_BUTTON = __image_resource('window_home.png')
WINDOW_BACK_BUTTON = __image_resource('window_back.png')
WINDOW_FORWARD_BUTTON = __image_resource('window_forward.png')
WINDOW_PAN_BUTTON = __image_resource('window_pan.png')
WINDOW_ZOOMTORECT_BUTTON = __image_resource('window_zoom_to_rect.png')
WINDOW_SAVE_BUTTON = __image_resource('window_filesave.png')
ANALYZE_IMAGE_BUTTON = __image_resource('IMG_ANALYZE_16.png')
STOP_ANALYSIS_BUTTON = __image_resource('stop.png')
PAUSE_ANALYSIS_BUTTON = __image_resource('IMG_PAUSE.png')


####################
#
# MENU HELP PATHS
#
####################
BATCH_PROCESSING_HELP_REF = """Help > Batch Processing"""
TEST_MODE_HELP_REF = """Help > Testing Your Pipeline"""
IMAGE_TOOLS_HELP_REF = """Help > Using Module Display Windows > How To Use The Image Tools"""
DATA_TOOL_HELP_REF = """Data Tools > Help"""
USING_YOUR_OUTPUT_REF = """Help > Using Your Output"""
MEASUREMENT_NAMING_HELP = """Help > Using Your Output > How Measurements are Named"""

####################
#
# MENU HELP CONTENT
#
####################
LEGACY_LOAD_MODULES_HELP = u"""\
The image loading modules **LoadImages** and **LoadSingleImage** are deprecated
and will be removed in a future version of CellProfiler. It is recommended you
choose to convert these modules as soon as possible. CellProfiler can do this
automatically for you when you import a pipeline using either of these legacy
modules.

Historically, these modules served the same functionality as the current
project structure (via **Images**, **Metadata**, **NamesAndTypes**, and **Groups**).
Pipelines loaded into CellProfiler that contain these modules will provide the option
of preserving them; these pipelines will operate exactly as before.

The section details information relevant for those who would like
to continue using these modules. Please note, however, that these
modules are deprecated and will be removed in a future version of CellProfiler.

Associating metadata with images
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Metadata (i.e., additional data about image data) is sometimes available
for input images. This information can be:

#. Used by CellProfiler to group images with common metadata identifiers
   (or “tags”) together for particular steps in a pipeline;
#. Stored in the output file along with CellProfiler-measured features
   for annotation or sample-tracking purposes;
#. Used to name additional input/output files.

Metadata is provided in the image filename or location (pathname). For
example, images produced by an automated microscope can be given
names such as “Experiment1\_A01\_w1\_s1.tif” in which the metadata
about the plate (“Experiment1”), the well (“A01”), the wavelength
number (“w1”) and the imaging site (“s1”) are captured. The name
of the folder in which the images are saved may be meaningful and may
also be considered metadata as well. If this is the case for your
data, use **LoadImages** to extract this information for use in the
pipeline and storage in the output file.

Details for the metadata-specific help is given next to the appropriate
settings in **LoadImages**, as well the specific
settings in other modules which can make use of metadata. However, here
is an overview of how metadata is obtained and used.

In **LoadImages**, metadata can be extracted from the filename and/or
folder location using regular expression, a specialized syntax used for
text pattern-matching. These regular expressions can be used to identify
different parts of the filename / folder. The syntax
*(?P<fieldname>expr)* will extract whatever matches *expr* and assign it
to the image’s *fieldname* measurement. A regular expression tool is
available which will allow you to check the accuracy of your regular
expression.

For instance, say a researcher has folder names with the date and
subfolders containing the images with the run ID (e.g.,
*./2009\_10\_02/1234/*). The following regular expression will capture
the plate, well and site in the fields *Date* and *Run*:
``.\*[\\\\\\/](?P<Date>.\\*)[\\\\\\\\/](?P<Run>.\\*)$``

=============   ============
Subexpression   Explanation
=============   ============
.\\*[\\\\\\\\/]      Skip characters at the beginning of the pathname until either a slash (/) or backslash (\\\\) is encountered (depending on the OS). The extra slash for the backslash is used as an escape sequence.
(?P<Date>       Name the captured field *Date*
.\\*             Capture as many characters that follow
[\\\\\\\\/]         Discard the slash/backslash character
(?P<Run>        Name the captured field *Run*
$               The *Run* field must be at the end of the path string, i.e., the last folder on the path. This also means that the *Date* field contains the parent folder of the *Date* folder.
=============   ============

In **LoadImages**, metadata is extracted from the image *File name*,
*Path* or *Both*. File names or paths containing “Metadata” can be used
to group files loaded by **LoadImages** that are associated with a common
metadata value. The files thus grouped together are then processed as a
distinct image set.

For instance, an experiment might require that images created on the
same day use an illumination correction function calculated from all
images from that day, and furthermore, that the date be captured in the
file names for the individual image sets specifying the illumination
correction functions.

In this case, if the illumination correction images are loaded with the
**LoadImages** module, **LoadImages** should be set to extract the metadata
tag from the file names. The pipeline will then match the individual images
with their corresponding illumination correction functions based on matching
“Metadata\_Date” fields.

Using image grouping
~~~~~~~~~~~~~~~~~~~~

To use grouping, you must define the relevant metadata for each image.
This can be done using regular expressions in **LoadImages**.

To use image grouping in **LoadImages**, please note the following:

-  *Metadata tags must be specified for all images listed.* You cannot
   use grouping unless an appropriate regular expression is defined for
   all the images listed in the module.
-  *Shared metadata tags must be specified with the same name for each
   image listed.* For example, if you are grouping on the basis of a
   metadata tag “Plate” in one image channel, you must also specify the
   “Plate” metadata tag in the regular expression for the other channels
   that you want grouped together.
"""

USING_THE_OUTPUT_FILE_HELP = u"""\
Please note that the output file will be deprecated in the future. This
setting is temporarily present for those needing HDF5 or MATLAB formats,
and will be moved to Export modules in future versions of CellProfiler.

The *output file* is a file where all information about the analysis as
well as any measurements will be stored to the hard drive. **Important
note:** This file does *not* provide the same functionality as the
Export modules. If you want to produce a spreadsheet of measurements
easily readable by Excel or a database viewer (or similar programs),
please refer to the **ExportToSpreadsheet** or **ExportToDatabase**
modules and the associated help.

The options associated with the output file are accessible by pressing
the “View output settings” button at the bottom of the pipeline panel.
In the settings panel to the left, in the *Output Filename* box, you can
specify the name of the output file.

The output file can be written in one of two formats:

-  A *.mat file* which is readable by CellProfiler and by `MATLAB`_
   (Mathworks).
-  An *.h5 file* which is readable by CellProfiler, MATLAB and any other
   program capable of reading the HDF5 data format. Documentation on how
   measurements are stored and handled in CellProfiler using this format
   can be found `here`_.

Results in the output file can also be accessed or exported using **Data
Tools** from the main menu of CellProfiler. The pipeline with its
settings can be be loaded from an output file using *File > Load
Pipeline…*

The output file will be saved in the Default Output Folder unless you
type a full path and file name into the file name box. The path must not
have spaces or characters disallowed by your computer’s platform.

If the output filename ends in *OUT.mat* (the typical text appended to
an output filename), CellProfiler will prevent you from overwriting this
file on a subsequent run by generating a new file name and asking if you
want to use it instead. You can override this behavior by checking the
*Allow overwrite?* box to the right.

For analysis runs that generate a large number of measurements, you may
notice that even though the analysis completes, CellProfiler continues
to use an inordinate amount of your CPU and RAM. This is because the
output file is written after the analysis is completed and can take a
very long time for a lot of measurements. If you do not need this file,
select "*Do not write measurements*" from
the “Measurements file format” drop-down box.

.. _MATLAB: http://www.mathworks.com/products/matlab/
.. _here: http://github.com/CellProfiler/CellProfiler/wiki/Module-structure-and-data-storage-retrieval#HDF5
"""

MATLAB_FORMAT_IMAGES_HELP = u"""\
Previous versions of CellProfiler supported reading and writing of MATLAB
format (.mat) images. MATLAB format images were useful for exporting
illumination correction functions generated by **CorrectIlluminationCalculate**.
These images could be loaded and applied to other pipelines using
**CorrectIlluminationApply**.

This version of CellProfiler no longer supports exporting MATLAB format
images. Instead, the recommended image format for illumination correction
functions is NumPy (.npy). Loading MATLAB format images is deprecated and
will be removed in a future version of CellProfiler. To ensure compatibility
with future versions of CellProfiler you can convert your .mat files to .npy
files via **SaveImages** using this version of CellProfiler.

See **SaveImages** for more details on saving NumPy format images.
"""

BUILDING_A_PIPELINE_HELP = u"""\
A *pipeline* is a sequential set of image analysis modules. The best way
to learn how to use CellProfiler is to load an example pipeline from the
CellProfiler website’s Examples page and try it with its included images,
then adapt it for
your own images. You can also build a pipeline from scratch. Click the
*Help* |HelpContent_BuildPipeline_image0|  button in the main window to get help for a specific
module.

Loading an existing pipeline
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. Put the images and pipeline into a folder on your computer.
#. Set the Default Output Folder (press the “View output settings”) to
   the folder where you want to place your output (preferably a
   different location than in the input images).
#. Load the pipeline using *File > Import Pipeline > From File…* in the
   main menu of CellProfiler, or drag and drop it to the pipeline window.
#. Click the *Analyze Images* button to start processing.
#. Examine the measurements using *Data tools*. The *Data tools* options
   are accessible in the main menu of CellProfiler and allow you to
   plot, view, or export your measurements (e.g., to Excel).
#. Alternately, you can load data into CellProfiler Analyst for more
   complex analysis. Please refer to its help for instructions.
#. If you modify the modules or settings in the pipeline, you can save
   the pipeline using *File > Export > Pipeline…*. Alternately, you can
   save the project as a whole using *File > Save Project* or *Save
   Project As…* which also saves the file list, i.e., the list of images.
#. To learn how to use a cluster of computers to process large batches
   of images, see *{BATCH_PROCESSING_HELP_REF}*.

Building a pipeline from scratch
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Constructing a pipeline involves placing individual modules into a
pipeline. The list of modules in the pipeline is shown in the *pipeline
panel* (located on the left-hand side of the CellProfiler window).

#. *Place analysis modules in a new pipeline.*

   Choose image analysis modules to add to your pipeline by clicking the
   *Add* |HelpContent_BuildPipeline_image1| button (located underneath the pipeline panel) or
   right-clicking in the pipeline panel itself and selecting a module
   from the pop-up box that appears.

   You can learn more about each module by clicking *Module Help* in the
   “Add modules” window or the *?* button after the module has been
   placed and selected in the pipeline. Modules are added to the end of
   the pipeline or after the currently selected module, but you can
   adjust their order in the main window by dragging and dropping them,
   or by selecting a module (or modules, using the *Shift* key) and
   using the *Move Module Up* |HelpContent_BuildPipeline_image2| and *Move Module Down*
   |HelpContent_BuildPipeline_image3| buttons. The *Remove Module* |HelpContent_BuildPipeline_image4| button will delete the
   selected module(s) from the pipeline.

   Most pipelines depend on one major step: identifying the objects,
   (otherwise known as “segmentation”). In
   CellProfiler, the objects you identify are called *primary*,
   *secondary*, or *tertiary*:

   -  **IdentifyPrimary** modules identify objects without relying on
      any information other than a single grayscale input image (e.g.,
      nuclei are typically primary objects).
   -  **IdentifySecondaryObjects** modules require a grayscale image
      plus an image where primary objects have already been identified,
      because the secondary objects are determined based on the primary
      objects (e.g., cells can be secondary objects when their
      identification is based on the location of nuclei).
   -  **IdentifyTertiary** modules require images in which two sets of
      objects have already been identified (e.g., nuclei and cell
      regions are used to define cytoplasm objects, which are
      tertiary objects).

#. *Adjust the settings in each module.*

   In the CellProfiler main window, click a module in the pipeline to
   see its settings in the settings panel. To learn more about the
   settings for each module, select the module in the pipeline and
   click the *Help* button to the right of each setting, or at the
   bottom of the pipeline panel for the help for all the settings for
   that module.

   If there is an error with the settings (e.g., a setting refers to an
   image that doesn’t exist yet), a |HelpContent_BuildPipeline_image5| icon will appear next to the
   module name. If there is a warning (e.g., a special notification
   attached to a choice of setting), a |HelpContent_BuildPipeline_image6| icon will appear. Errors
   will cause the pipeline to fail upon running, whereas a warning will
   not. Once the errors/warnings have been resolved, a |HelpContent_BuildPipeline_image7|  icon will
   appear indicating that the module is ready to run.

#. *Set your Default Output Folder and, if necessary, your Default Input Folder*

   Both of these can be set via *File > Preferences…*.  Default Output Folder can
   be additionally changed by clicking the *View output settings* button directly
   below the list of modules in the pipeline; if any modules in your pipeline have
   referenced the Default Input Folder it will also appear in *View output settings*.

#. *Click *Analyze images* to start processing.*

   All of the images in your selected folder(s) will be analyzed using
   the modules and settings you have specified. The bottom of the
   CellProfiler window will show:

   -  A *pause button* |HelpContent_BuildPipeline_image8|  which pauses execution and allows you
      to subsequently resume the analysis.
   -  A *stop button* |HelpContent_BuildPipeline_image9|  which cancels execution after prompting
      you for a place to save the measurements collected to that point.
   -  A *progress bar* which gives the elapsed time and estimates the
      time remaining to process the full image set.

   At the end of each cycle:

   -  If you are creating a MATLAB or HDF5 output file, CellProfiler saves the measurements in the output file.
   -  If you are using the **ExportToDatabase** module, CellProfiler saves the measurements in the
      output database.
   -  If you are using the **ExportToSpreadsheet** module, CellProfiler saves the measurements *into a
      temporary file*; spreadsheets are not written until all modules have been processed.

#. *Click *Start Test Mode* to preview results.*

   You can optimize your pipeline by selecting the *Test* option from
   the main menu. Test mode allows you to run the pipeline on a
   selected image, preview the results, and adjust the module settings
   on the fly. See *{TEST_MODE_HELP_REF}* for more details.

#. Save your project (which includes your pipeline) via *File > Save
   Project*.

*Saving images in your pipeline:* Due to the typically high number of
intermediate images produced during processing, images produced during
processing are not saved to the hard drive unless you specifically
request it, using a **SaveImages** module.

*Saving data in your pipeline:* You can include an **Export** module to
automatically export data in a format you prefer. See
*{USING_YOUR_OUTPUT_REF}* for more details.

.. |HelpContent_BuildPipeline_image0| image:: {MODULE_HELP_BUTTON}
.. |HelpContent_BuildPipeline_image1| image:: {MODULE_ADD_BUTTON}
.. |HelpContent_BuildPipeline_image2| image:: {MODULE_MOVEUP_BUTTON}
.. |HelpContent_BuildPipeline_image3| image:: {MODULE_MOVEDOWN_BUTTON}
.. |HelpContent_BuildPipeline_image4| image:: {MODULE_REMOVE_BUTTON}
.. |HelpContent_BuildPipeline_image5| image:: {SETTINGS_ERROR_ICON}
.. |HelpContent_BuildPipeline_image6| image:: {SETTINGS_WARNING_ICON}
.. |HelpContent_BuildPipeline_image7| image:: {SETTINGS_OK_ICON}
.. |HelpContent_BuildPipeline_image8| image:: {RUNSTATUS_PAUSE_BUTTON}
.. |HelpContent_BuildPipeline_image9| image:: {RUNSTATUS_STOP_BUTTON}
""".format(**{
    "BATCH_PROCESSING_HELP_REF": BATCH_PROCESSING_HELP_REF,
    "MODULE_ADD_BUTTON": MODULE_ADD_BUTTON,
    "MODULE_HELP_BUTTON": MODULE_HELP_BUTTON,
    "MODULE_MOVEDOWN_BUTTON": MODULE_MOVEDOWN_BUTTON,
    "MODULE_MOVEUP_BUTTON": MODULE_MOVEUP_BUTTON,
    "MODULE_REMOVE_BUTTON": MODULE_REMOVE_BUTTON,
    "RUNSTATUS_PAUSE_BUTTON": RUNSTATUS_PAUSE_BUTTON,
    "RUNSTATUS_SAVE_BUTTON": RUNSTATUS_SAVE_BUTTON,
    "RUNSTATUS_STOP_BUTTON": RUNSTATUS_STOP_BUTTON,
    "SETTINGS_ERROR_ICON": SETTINGS_ERROR_ICON,
    "SETTINGS_OK_ICON": SETTINGS_OK_ICON,
    "SETTINGS_WARNING_ICON": SETTINGS_WARNING_ICON,
    "TEST_MODE_HELP_REF": TEST_MODE_HELP_REF,
    "USING_YOUR_OUTPUT_REF": USING_YOUR_OUTPUT_REF
})

SPREADSHEETS_DATABASE_HELP = u"""\
CellProfiler can save measurements as a *spreadsheet* or as a *database*.
Which format you use will depend on some of the considerations below:

-  *Learning curve:* Applications that handle spreadsheets (e.g., Excel,
   `Calc`_ or `Google Docs`_) are easy for beginners to use. Databases
   are more sophisticated and require knowledge of specialized languages
   (e.g., MySQL, Oracle, etc); a popular freeware access tool is
   `SQLyog`_.
-  *Capacity and speed:* Databases are designed to hold larger amounts
   of data than spreadsheets. Spreadsheets may contain a few
   thousand rows of data, whereas databases can hold many millions of
   rows of data. Accessing a particular portion of data in a database
   is optimized for speed.
-  *Downstream application:* If you wish to use Excel or another simple
   tool to analyze your data, a spreadsheet is likely the best choice.  If you
   intend to use CellProfiler Analyst, you must create a database.  If you
   plan to use a scripting language, most languages have ways to import
   data from either format.

.. _Calc: http://www.libreoffice.org/discover/calc/
.. _Google Docs: http://docs.google.com
.. _SQLyog: http://www.webyog.com/
"""

MEMORY_AND_SPEED_HELP = u"""\
If you find that you are running into out-of-memory errors and/or speed
issues associated with your analysis run, check out a number of
solutions on our forum `FAQ`_ .

.. _FAQ: http://forum.cellprofiler.org
"""

RUNNING_YOUR_PIPELINE_HELP = u"""\
Once you have tested your pipeline using Test mode and you are satisfied
with the module settings, you are ready to run the pipeline on your
entire set of images. To do this:

-  Exit Test mode by clicking the “Exit Test Mode” button or selecting
   *Test > Exit Test Mode*.
-  Click the "|HelpContent_RunningPipeline_image0| Analyze Images" button and begin processing your
   data sets.

During the analysis run, the progress will appear in the status bar at
the bottom of CellProfiler. It will show you the total number of image
sets, the number of image sets completed, the time elapsed and the
approximate time remaining in the run.

If you need to pause analysis, click the "|HelpContent_RunningPipeline_image1| Pause" button, then
click the “Resume” button to continue. If you want to terminate
analysis, click the "|HelpContent_RunningPipeline_image2| Stop Analysis" button.

If your computer has multiple processors, CellProfiler will take
advantage of them by starting multiple copies of itself to process the
image sets in parallel. You can set the number of *workers* (i.e., copies
of CellProfiler activated) under *File > Preferences…*

.. |HelpContent_RunningPipeline_image0| image:: {ANALYZE_IMAGE_BUTTON}
.. |HelpContent_RunningPipeline_image1| image:: {PAUSE_ANALYSIS_BUTTON}
.. |HelpContent_RunningPipeline_image2| image:: {STOP_ANALYSIS_BUTTON}
""".format(**{
    "ANALYZE_IMAGE_BUTTON": ANALYZE_IMAGE_BUTTON,
    "PAUSE_ANALYSIS_BUTTON": PAUSE_ANALYSIS_BUTTON,
    "STOP_ANALYSIS_BUTTON": STOP_ANALYSIS_BUTTON
})

BATCHPROCESSING_HELP = u"""\
CellProfiler is designed to analyze images in a high-throughput manner.
Once a pipeline has been established for a set of images, CellProfiler
can export files that enable batches of images to be analyzed on a
computing cluster with the pipeline.

It is possible to process tens or even hundreds of thousands of images
for one analysis in this manner. We do this by breaking the entire set
of images into separate batches, then submitting each of these batches
as individual jobs to a cluster. Each individual batch can be separately
analyzed from the rest.

The following describes the workflow for running your pipeline on a cluster
that's physically located at your local institution; for running in a cloud-based
cluster using Amazon Web Services, please see our `blog post`_ on Distributed
CellProfiler, a tool designed to streamline that process.

Submitting files for batch processing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Below is a basic workflow for submitting your image batches to a
cluster.

#. *Create a folder for your project on your cluster.* For
   high-throughput analysis, it is recommended to create a separate
   project folder for each run.
#. Within this project folder, create the following folders (both of
   which must be connected to the cluster computing network):

   -  Create an input folder, then transfer all of your images to this
      folder as the input folder. The input folder must be readable by
      everyone (or at least your cluster) because each of the separate
      cluster computers will read input files from this folder.
   -  Create an output folder where all your output data will be stored.
      The output folder must be writeable by everyone (or at least your
      cluster) because each of the separate cluster computers will write
      output files to this folder.

   If you cannot create folders and set read/write permissions to these
   folders (or do not know how), ask your Information Technology (IT)
   department for help.
#. Press the “{VIEW_OUTPUT_SETTINGS_BUTTON_NAME}” button. In the
   panel that appears, set the Default Input and Default Output Folders
   to the *images* and *output* folders created above, respectively. The
   Default Input Folder setting will only appear if a legacy pipeline is
   being run.
#. *Create a pipeline for your image set.* You should test it on a few
   example images from your image set (if you are unfamilar with the
   concept of an image set, please see the help for the **Input**
   modules). The module settings selected for your pipeline will be
   applied to *all* your images, but the results may vary depending on
   the image quality, so it is critical to ensure your settings are
   robust against your “worst-case” images.
   For instance, some images may contain no cells. If this happens, the
   automatic thresholding algorithms will incorrectly choose a very low
   threshold, and therefore “find” spurious objects. This can be
   overcome by setting a lower limit on the threshold in the
   **IdentifyPrimaryObjects** module.
   The Test mode in CellProfiler may be used for previewing the results
   of your settings on images of your choice. Please refer to
   *{TEST_MODE_HELP_REF}* for more details on how to use this
   utility.
#. *Add the CreateBatchFiles module to the end of your pipeline.*
   This module is needed to resolve the pathnames to your files with
   respect to your local machine and the cluster computers. If you are
   processing large batches of images, you may also consider adding
   **ExportToDatabase** to your pipeline, after your measurement modules
   but before the CreateBatchFiles module. This module will export your
   data either directly to a MySQL/SQLite database or into a set of
   comma-separated files (CSV) along with a script to import your data
   into a MySQL database. Please refer to the help for these modules in
   order learn more about which settings are appropriate.
#. *Run the pipeline to create a batch file.* Click the *Analyze images*
   button and the analysis will begin processing locally. Do not be
   surprised if this initial step takes a while: CellProfiler must
   first create the entire image set list based on your settings in the
   **Input** modules (this process can be sped up by creating your list
   of images as a CSV and using the **LoadData** module to load it).
   With the **CreateBatchFiles** module in place, the pipeline will not
   process all the images, but instead will create a batch file (a file
   called *Batch\_data.h5*) and save it in the Default Output Folder
   (Step 1). The advantage of using **CreateBatchFiles** from the
   researcher’s perspective is that the Batch\_data.h5 file generated by
   the module captures all of the data needed to run the analysis. You
   are now ready to submit this batch file to the cluster to run each of
   the batches of images on different computers on the cluster.
#. *Submit your batches to the cluster.* Log on to your cluster, and
   navigate to the directory where you have installed CellProfiler on
   the cluster.
   A single batch can be submitted with the following command:

   .. code-block::

      ./python -m cellprofiler -p <Default_Output_Folder_path>/Batch_data.h5 \\
      -c -r -b \\
      -f <first_image_set_number> \\
      -l <last_image_set_number>

   This command submits the batch file to CellProfiler and specifies
   that CellProfiler run in a batch mode without its user interface to
   process the pipeline. This run can be modified by using additional
   options to CellProfiler that specify the following:

   -  ``-p <Default_Output_Folder_path>/Batch_data.h5``: The
      location of the batch file, where ``<Default\_Output\_Folder\_path>``
      is the output folder path as seen by the cluster computer.
   -  ``-c``: Run “headless”, i.e., without the GUI
   -  ``-r``: Run the pipeline specified on startup, which is contained
      in the batch file.
   -  ``-b``: Do not build extensions, since by this point, they should
      already be built.
   -  ``-f <first_image_set_number>``: Start processing with the image
      set specified, <first\_image\_set\_number>
   -  ``-l <last_image_set_number>``: Finish processing with the image
      set specified, <last\_image\_set\_number>

   Typically, a user will break a long image set list into pieces and
   execute each of these pieces using the command line switches, ``-f``
   and ``-l`` to specify the first and last image sets in each job. A
   full image set would then need a script that calls CellProfiler with
   these options with sequential image set numbers, e.g, 1-50, 51-100,
   etc to submit each as an individual job.

   If you need help in producing the batch commands for submitting your
   jobs, use the ``--get-batch-commands`` along with the ``-p`` switch to
   specify the Batch\_data.h5 file output by the CreateBatchFiles module.
   When specified, CellProfiler will output one line to the terminal per
   job to be run. This output should be further processed to generate a
   script that can invoke the jobs in a cluster-computing context.

   The above notes assume that you are running CellProfiler using our
   source code (see “Developer’s Guide” under Help for more details). If
   you are using the compiled version, you would replace
   ``./python -m cellprofiler`` with the CellProfiler executable
   file itself and run it from the installation folder.

Once all the jobs are submitted, the cluster will run each batch
individually and output any measurements or images specified in the
pipeline. Specifying the output filename using the ``-o`` switch when
calling CellProfiler will also produce an output file containing the
measurements for that batch of images in the output folder. Check the
output from the batch processes to make sure all batches complete.
Batches that fail for transient reasons can be resubmitted.

To see a listing and documentation for all available arguments to
CellProfiler, type``cellprofiler --help``.

For additional help on batch processing, refer to our `wiki`_ if
installing CellProfiler on a Unix system, our
`wiki <http://github.com/CellProfiler/CellProfiler/wiki/Adapting-CellProfiler-to-a-LIMS-environment>`__ on adapting CellProfiler to a LIMS
environment, or post your questions on the CellProfiler `CPCluster
forum`_.

.. _wiki: http://github.com/CellProfiler/CellProfiler/wiki/Source-installation-%28Linux%29
.. _CPCluster forum: http://forum.cellprofiler.org/c/cellprofiler/cpcluster-help
.. _blog post: http://blog.cellprofiler.org/2016/12/28/making-it-easier-to-run-image-analysis-in-the-cloud-announcing-distributed-cellprofiler/
""".format(**{
    "TEST_MODE_HELP_REF": TEST_MODE_HELP_REF,
    "VIEW_OUTPUT_SETTINGS_BUTTON_NAME": VIEW_OUTPUT_SETTINGS_BUTTON_NAME
})

RUN_MULTIPLE_PIPELINES_HELP = u"""\
The **Run multiple pipelines** dialog lets you select several
pipelines which will be run consecutively. Please note the following:

-  Pipeline files (.cppipe) are supported.
-  Project files (.cpproj) from CellProfiler 2.1 or newer are not supported.
   To convert your project to a pipeline (.cppipe), select *File > Export > Pipeline…*
   and, under the “Save as type” dropdown, select “CellProfiler pipeline and file list”
   to export the project file list with the pipeline.

You can invoke **Run multiple pipelines** by selecting it from the file menu. The dialog has three parts to it:

-  *File chooser*: The file chooser lets you select the pipeline files
   to be run. The *Select all* and *Deselect all* buttons to the right
   will select or deselect all pipeline files in the list. The *Add*
   button will add the pipelines to the pipeline list. You can add a
   pipeline file multiple times, for instance if you want to run that
   pipeline on more than one input folder.
-  *Directory chooser*: The directory chooser lets you navigate to
   different directories. The file chooser displays all pipeline files
   in the directory chooser’s current directory.
-  *Pipeline list*: The pipeline list has the pipelines to be run in the
   order that they will be run. Each pipeline has a default input and
   output folder and a measurements file. You can change any of these by
   clicking on the file name - an appropriate dialog will then be
   displayed. You can click the remove button to remove a pipeline from
   the list.

CellProfiler will run all of the pipelines on the list when you hit
the “OK” button.
"""

CONFIGURING_LOGGING_HELP = u"""\
CellProfiler prints diagnostic messages to the console by default. You
can change this behavior for most messages by configuring logging. The
simplest way to do this is to use the command-line switch, “-L”, to
set the log level. For instance, to show error messages or more
critical events, start CellProfiler like this:
``CellProfiler -L ERROR``
The following is a list of log levels that can be used:

-  **DEBUG:** Detailed diagnostic information
-  **INFO:** Informational messages that confirm normal progress
-  **WARNING:** Messages that report problems that might need attention
-  **ERROR:** Messages that report unrecoverable errors that result in
   data loss or termination of the current operation.
-  **CRITICAL:** Messages indicating that CellProfiler should be
   restarted or is incapable of running.

You can tailor CellProfiler’s logging with much more control using a
logging configuration file. You specify the file name in place of the
log level on the command line, like this:

``CellProfiler -L ~/CellProfiler/my_log_config.cfg``

Files are in the Microsoft .ini format which is grouped into
categories enclosed in square brackets and the key/value pairs for
each category. Here is an example file:

::

    [loggers]
    keys=root,pipelinestatistics

    [handlers]
    keys=console,logfile

    [formatters]
    keys=detailed

    [logger_root]
    level=WARNING
    handlers=console

    [logger_pipelinestatistics]
    level=INFO
    handlers=logfile
    qualname=pipelineStatistics
    propagate=0

    [handler_console]
    class=StreamHandler
    formatter=detailed
    level=WARNING
    args=(sys.stderr)

    [handler_logfile]
    class=FileHandler
    level=INFO
    args=('~/CellProfiler/logfile.log','w')

    [formatter_detailed]
    format=[%(asctime)s] %(name)s %(levelname)s %(message)s
    datefmt=

The above file would print warnings and errors to the console for all
messages but “pipeline statistics” which are configured using the
*pipelineStatistics* logger are written to a file instead. The
pipelineStatistics logger is the logger that is used to print progress
messages when the pipeline is run. You can find out which loggers are
being used to write particular messages by printing all messages with a
formatter that prints the logger name (“%(name)s”).
The format of the file is described in greater detail `here`_.

.. _here: http://docs.python.org/2.7/howto/logging.html#configuring-logging
"""

ACCESSING_OMERO_IMAGES = u"""\
CellProfiler can load images from `OMERO`_. Please see CellProfiler's
`developer wiki`_ for instructions.

.. _OMERO: http://www.openmicroscopy.org/site/products/omero
.. _developer wiki: http://github.com/CellProfiler/CellProfiler/wiki/OMERO:-Accessing-images-from-CellProfiler

"""

MEASUREMENT_NOMENCLATURE_HELP = u"""\
In CellProfiler, measurements are exported as well as stored internally
using the following general nomenclature:
``MeasurementType_Category_SpecificFeatureName_Parameters``

Below is the description for each of the terms:

-  ``MeasurementType``: The type of data contained in the measurement,
   which can be one of three forms:

   -  *Per-image:* These measurements are image-based (e.g., thresholds,
      counts) and are specified with the name “Image” or with the
      measurement (e.g., “Mean”) for per-object measurements aggregated
      over an image.
   -  *Per-object:* These measurements are per-object and are specified
      as the name given by the user to the identified objects (e.g.,
      “Nuclei” or “Cells”).
   -  *Experiment:* These measurements are produced for a particular
      measurement across the entire analysis run (e.g., Z’ factors), and
      are specified with the name “Experiment”. See
      **CalculateStatistics** for an example.

-  ``Category:`` Typically, this information is specified in one of two
   ways:

   -  A descriptive name indicative of the type of measurement taken
      (e.g., “Intensity”)
   -  No name if there is no appropriate ``Category`` (e.g., if the
      *SpecificFeatureName* is “Count”, no ``Category`` is specfied).

-  ``SpecificFeatureName:`` The specific feature recorded by a module
   (e.g., “Perimeter”). Usually the module recording the measurement
   assigns this name, but a few modules allow the user to type in the
   name of the feature (e.g., the **CalculateMath** module allows the
   user to name the arithmetic measurement).
-  ``Parameters:`` This specifier is to distinguish measurements
   obtained from the same objects but in different ways. For example,
   **MeasureObjectIntensity** can measure intensities for “Nuclei” in
   two different images. This specifier is used primarily for data
   obtained from an individual image channel specified by the **Images**
   module or a legacy **Load** module (e.g., “OrigBlue” and “OrigGreen”)
   or a particular spatial scale (e.g., under the category “Texture” or
   “Neighbors”). Multiple parameters are separated by underscores.

   Below are additional details specific to various modules:

   -  Measurements from the *AreaShape* and *Math* categories do not
      have a ``Parameter`` specifier.
   -  Measurements from *Intensity*, *Granularity*, *Children*,
      *RadialDistribution*, *Parent* and *AreaOccupied* categories will
      have an associated image as the Parameter.
   -  *Measurements from the *Neighbors* and *Texture* category will
      have a spatial scale ``Parameter``.*
   -  Measurements from the *Texture* and *RadialDistribution*
      categories will have both a spatial scale and an image
      ``Parameter``.

As an example, consider a measurement specified as
``Nuclei_Texture_DifferenceVariance_ER_3``:

-  ``MeasurementType`` is “Nuclei,” the name given to the detected
   objects by the user.
-  ``Category`` is “Texture,” indicating that the module
   **MeasureTexture** produced the measurements.
-  ``SpecificFeatureName`` is “DifferenceVariance,” which is one of the
   many texture measurements made by the **MeasureTexture** module.
-  There are two ``Parameters``, the first of which is “ER”. “ER” is the
   user-provided name of the image in which this texture measurement was
   made.
-  The second ``Parameter`` is “3”, which is the spatial scale at which
   this texture measurement was made, according to the user-provided
   settings for the module.

See also the *Available measurements* heading under the main help for
many of the modules, as well as **ExportToSpreadsheet** and
**ExportToDatabase** modules.
"""

FIGURE_HELP = (
    ("Using The Display Window Menu Bar", read_content("display_menu_bar.rst")),
    ("Using The Interactive Navigation Toolbar", read_content("display_interactive_navigation.rst")),
    ("How To Use The Image Tools", read_content("display_image_tools.rst"))
)

CREATING_A_PROJECT_CAPTION = "Creating A Project"

PLATEVIEWER_HELP = u"""\
The plate viewer is a data tool that displays the images in your
experiment in plate format. Your project must define an image set list
with metadata annotations for the image’s well and, optionally its plate
and site. The plate viewer will then group your images by well and
display a plate map for you. If you have defined a plate metadata tag
(with the name, “Plate”), the plate viewer will group your images by
plate and display a choice box that lets you pick the plate to display.

Click on a well to see the images for that well. If you have more than
one site per well and have site metadata (with the name, “Site”), the
plate viewer will tile the sites when displaying, and the values under
“X” and “Y” determine the position of each site in the tiled grid.

The values for “Red”, “Green”, and “Blue” in each row are brightness
multipliers- changing the values will determine the color and scaling
used to display each channel. “Alpha” determines the weight each channel
contributes to the summed image.
"""
