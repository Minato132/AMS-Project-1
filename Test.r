library(ggplot2)
library(knitr)

data <- read.csv("Part B Data/binned_data2")
data1 <- data[,c('x', 'y')]


# fit full model
model1 <- lm(y ~ poly(x, 2), data = data1)

# fit reduced model
model2 <- lm(y ~ x, data = data1)

print(anova(model1, model2))

plot <- ggplot(data1, aes(x=x, y=y)) + geom_point() + stat_smooth(method = 'lm', formula = y ~ x, size = 1) + xlab('x') + ylab('y') 

M <- lm(y~x , data = data1)
print(summary(M))
print(confint(M, level = .995))
print(plot)