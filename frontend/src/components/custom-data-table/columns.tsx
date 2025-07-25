"use client"

import Image from "next/image";
import { ColumnDef } from "@tanstack/react-table";
import { Button } from "../ui/button";
import { User } from "lucide-react";
import { Badge } from "@/components/ui/badge";


export type ProfessionalTableData = {
    professional: {
        id: number;
        name: string;
        photo?: string
    }
    specialty: string[];
};


export const columns: ColumnDef<ProfessionalTableData>[] = [
    {
        accessorKey: "professional.name",
        header: "Profissional",
        cell: ({ row }) => {
            const { name, id, photo } = row.original.professional;
            return (
                <div className="flex items-center gap-3 ms-10">
                    {photo ? (
                        <Image
                            src={photo}
                            alt={name}
                            width={40}
                            height={40}
                            className="rounded-full object-cover"
                        />
                    ) : (
                        <div className="w-10 h-10 rounded-full bg-gray-200 flex items-center justify-center">
                            <User className="w-6 h-6 text-gray-400" />
                        </div>
                    )}
                    <div className="flex flex-col">
                        <span className="font-bold text-gray-900">{name}</span>
                        <span className="text-xs text-gray-500">ID: {id}</span>
                    </div>
                </div>
            );
        },
    },
    {
        accessorKey: "specialty",
        header: "Especialidade",
        cell: ({ row }) => (
            <div className="flex flex-wrap gap-2 justify-center">
                {row.original.specialty.map((spec) => (
                    <Badge key={spec} className="bg-dark-teal text-white font-medium">
                        {spec}
                    </Badge>
                ))}
            </div>
        ),
        className: "text-center",
    },
    {
        id: "actions",
        header: "Ações",
        cell: () => (
            <div className="flex gap-2 justify-center">
                <Button variant="outline">Editar</Button>
                <Button variant="outline" color="destructive">Excluir</Button>
            </div>
        ),
        className: "text-center",
    },
];