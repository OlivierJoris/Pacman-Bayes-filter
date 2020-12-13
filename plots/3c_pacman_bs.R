confused <- c(3.091, 3.486)
afraid <- c(2.371, 2.012)
scared <- c(1.125, 0.994)

colors <- c("blue", "green", "blue", "green", "blue", "green")

barplot(cbind(confused, afraid, scared), beside = TRUE, names.arg = c("confused", "afraid", "scared"), col = colors, ylim = c(0,5), main = "Mean entropy of Pacman's belief state", ylab = "Mean entropy")
legend("topright", legend = c("large_filter layout", "large_filter_walls layout"), col=c("blue", "green"), pch = c(15,15))

arrows(x0=1.5, y0= 3.091 - 0.547, x1=1.5, y1= 3.091 + 0.547, code=3, angle=90, length=0.2, col="black", lwd=2)
text(1.5, 0.2,round(3.091, digits=3), srt=0, col = "black")

arrows(x0=2.5, y0= 3.486 - 0.536, x1=2.5, y1= 3.486 + 0.536, code=3, angle=90, length=0.2, col="black", lwd=2)
text(2.5, 0.2,round(3.486, digits=3), srt=0, col = "black")

arrows(x0=4.5, y0= 2.371 - 0.647, x1=4.5, y1= 2.371 + 0.647, code=3, angle=90, length=0.2, col="black", lwd=2)
text(4.5, 0.2,round(2.371, digits=3), srt=0, col = "black")

arrows(x0=5.5, y0= 2.012 - 0.927, x1=5.5, y1= 2.012 + 0.927, code=3, angle=90, length=0.2, col="black", lwd=2)
text(5.5, 0.2,round(2.012, digits=3), srt=0, col = "black")

arrows(x0=7.5, y0= 1.125 - 0.382, x1=7.5, y1= 1.125 + 0.382, code=3, angle=90, length=0.2, col="black", lwd=2)
text(7.5, 0.2,round(1.125, digits=3), srt=0, col = "black")

arrows(x0=8.5, y0= 0.994 - 0.523, x1=8.5, y1= 0.994 + 0.523, code=3, angle=90, length=0.2, col="black", lwd=2)
text(8.5, 0.2,round(0.994, digits=3), srt=0, col = "black")

