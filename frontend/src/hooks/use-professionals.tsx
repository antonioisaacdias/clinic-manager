import { useQuery } from "@tanstack/react-query";
import type { ProfessionalTableData } from "@/components/custom-data-table/columns";
import api from "@/services/api";

export function useProfessionals() {
  return useQuery<ProfessionalTableData[]>({
    queryKey: ["professionals"],
    queryFn: async () => {
      const { data } = await api.get("professionals/");
      return data.map((item: any) => ({
        professional: {
          id: item.uuid,
          name: item.name,
          photo: item.photo,
        },
        specialty: item.specialties,
      }));
    },
  });
}