import os
import argparse

parser = argparse.ArgumentParser("make latex figures for systs")
parser.add_argument("match", type=str,
                    help="string which must be included in shortname")
args = parser.parse_args()

imgDir = "figures/systs/prediction/"

fdMCImgs = [os.path.join(imgDir, img) for img in os.listdir(imgDir)
                                      if "fd_mc_" in img]
figText = """
\\begin{figure}
\\begin{center}
\\begin{subfigure}[c]{0.49\\textwidth}
\\includegraphics[width=\\textwidth]{%s}
\\caption*{FD MC Prediction}
\\end{subfigure}
\\begin{subfigure}[c]{0.49\\textwidth}
\\includegraphics[width=\\textwidth]{%s}
\\caption*{ND MC Prediction and Data}
\\end{subfigure}

\\vspace{20pt}

\\begin{subfigure}[c]{0.49\\textwidth}
\\includegraphics[width=\\textwidth]{%s}
\\caption*{Extrapolated FD Prediction}
\\end{subfigure}
\\begin{subfigure}[c]{0.49\\textwidth}
\\includegraphics[width=\\textwidth]{%s}
\\caption*{90 hashtagpercent Confidence Interval}
\\end{subfigure}
\end{center}
\caption{Systematic effect of %s uncertainty}{
Systematic effects can be seen in the predictions and confidence intervals
which result.
The top left pane shows the FD prediction, while the top right shows the
ND prediction and ND data overlaid in black.
The result of the extrapolation is shown in the bottom left, in which
systematic uncertainties can cancel.
The bottom right pane shows 90 hashtagpercent confidence intervals with and without
the effect of the systematic error.}
\label{syst_fig_%s}

\end{figure}

"""
for fdMCImg in fdMCImgs:
  ndMCImg = fdMCImg.replace("fd_mc_", "nd_mc_")
  fdExtrapImg = fdMCImg.replace("fd_mc_", "fd_extrap_")
  fdContourImg = fdExtrapImg.replace("_prediction_", "_contour_")
  shortname = os.path.splitext(fdMCImg)[0].split("_")[-1]
  if not args.match in shortname: continue
  print figText % (fdMCImg, ndMCImg, fdExtrapImg, fdContourImg,
                   shortname, shortname)
