variable "app_name" {}

variable "vpc_id" {}

variable "ingress_ports" {
  type        = list(number)
  description = "list of ingress ports"
  default     = [80, 443]
}
