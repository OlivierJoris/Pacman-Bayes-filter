confused <- c(3.3815262204238214, 3.2012568760391544)
afraid <- c(2.034467593791203, 2.521565219083069)
scared <- c(1.1547196316061477, 3.06720814248804)

colors <- c("blue", "green", "blue", "green", "blue", "green")

barplot(cbind(confused, afraid, scared), beside = TRUE, names.arg = c("confused", "afraid", "scared"), col = colors, ylim = c(0,5), main = "Mean entropy of Pacman belief state", ylab = "Mean entropy")
legend("topright", legend = c("large_filter layout", "large_filter_walls layout"), col=c("blue", "green"), pch = c(15,15))

arrows(x0=1.5, y0= 3.3815262204238214 - 1.091022535004305, x1=1.5, y1= 3.3815262204238214 + 1.091022535004305, code=3, angle=90, length=0.2, col="black", lwd=2)
text(1.5, 0.5,round(3.3815262204238214, digits=3), srt=90, col = "black")

arrows(x0=2.5, y0= 3.2012568760391544 - 0.6824390030049029, x1=2.5, y1= 3.2012568760391544 + 0.6824390030049029, code=3, angle=90, length=0.2, col="black", lwd=2)
text(2.5, 0.5,round(3.2012568760391544, digits=3), srt=90, col = "black")

arrows(x0=4.5, y0= 2.034467593791203 - 0.7683511927567366, x1=4.5, y1= 2.034467593791203 + 0.7683511927567366, code=3, angle=90, length=0.2, col="black", lwd=2)
text(4.5, 0.5,round(2.034467593791203, digits=3), srt=90, col = "black")

arrows(x0=5.5, y0= 2.521565219083069 - 0.8501433756196101, x1=5.5, y1= 2.521565219083069 + 0.8501433756196101, code=3, angle=90, length=0.2, col="black", lwd=2)
text(5.5, 0.5,round(2.521565219083069, digits=3), srt=90, col = "black")

arrows(x0=7.5, y0= 1.1547196316061477 - 0.6711016173217386, x1=7.5, y1= 1.1547196316061477 + 0.6711016173217386, code=3, angle=90, length=0.2, col="black", lwd=2)
text(7.15, 0.5,round(1.1547196316061477, digits=3), srt=90, col = "black")

arrows(x0=8.5, y0= 3.06720814248804 - 0.8223786784786498, x1=8.5, y1= 3.06720814248804 + 0.8223786784786498, code=3, angle=90, length=0.2, col="black", lwd=2)
text(8.5, 0.5,round(3.06720814248804, digits=3), srt=90, col = "black")

