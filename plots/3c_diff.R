confused <- c(4.983, 4.832)
afraid <- c(1.930, 1.760)
scared <- c(0.891, 0.812)

colors <- c("blue", "green", "blue", "green", "blue", "green")

barplot(cbind(confused, afraid, scared), beside = TRUE, names.arg = c("confused", "afraid", "scared"), col = colors, ylim = c(0,9), main = "Mean quality of Pacman's belief state", ylab = "Mean quality")
legend("topright", legend = c("large_filter layout", "large_filter_walls layout"), col=c("blue", "green"), pch = c(15,15))

arrows(x0=1.5, y0= 4.983 - 2.102, x1=1.5, y1= 4.983 + 2.102, code=3, angle=90, length=0.2, col="black", lwd=2)
text(1.5, 0.2,round(4.983, digits=3), srt=0, col = "black")

arrows(x0=2.5, y0= 4.832 - 2.183, x1=2.5, y1= 4.832 + 2.183, code=3, angle=90, length=0.2, col="black", lwd=2)
text(2.5, 0.2,round(4.832, digits=3), srt=0, col = "black")

arrows(x0=4.5, y0= 1.930 - 0.799, x1=4.5, y1= 1.930 + 0.799, code=3, angle=90, length=0.2, col="black", lwd=2)
text(4.5, 0.2,round(1.930, digits=3), srt=0, col = "black")

arrows(x0=5.5, y0= 1.760 - 1.329, x1=5.5, y1= 1.760 + 1.329, code=3, angle=90, length=0.2, col="black", lwd=2)
text(5.5, 0.2,round(1.760, digits=3), srt=0, col = "black")

arrows(x0=7.5, y0= 0.891 - 0.495, x1=7.5, y1= 0.891 + 0.495, code=3, angle=90, length=0.2, col="black", lwd=2)
text(7.5, 0.2,round(0.891, digits=3), srt=0, col = "black")

arrows(x0=8.5, y0= 0.812 - 0.421, x1=8.5, y1= 0.812 + 0.421, code=3, angle=90, length=0.2, col="black", lwd=2)
text(8.5, 0.2,round(0.812, digits=3), srt=0, col = "black")












