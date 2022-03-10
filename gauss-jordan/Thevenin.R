#vector
RL <- seq(from=0, to=100, by=0.5)

#definición de constantes
Vth <- 26.2
Rth<-10.07

#culcular irl, vrl
iRL<-Vth / (Rth + RL)
vRL<-iRL*RL

#######calcular potecias

P_RL<-iRL*vRL

P_max<-max(P_RL)
Index<-match(P_max, P_RL)
Rp_max<-RL[Index]


######graficar corriente y tensión

plot(RL, iRL, xlab="Resistencia RL", ylab="Corriente iRL", type="l", col="blue")
plot(RL, vRL, xlab="Resistencia RL", ylab="Voltaje vRL", type="l", col="blue")
plot(RL, P_RL, xlab="Resistencia RL", ylab="Potencia", type="l", col="blue")

##c() es vector
points(Rp_max, P_max, col="red", type="o")
lines(c(0, Rp_max), c(P_max, P_max), lty=2)
lines(c(Rp_max, Rp_max), c(0, P_max), lty=2)

e1<-paste("P_max= ", toString(P_max))
e2<-paste("Rp_max= ", Rp_max)
legend("topright", c(e1, e2))



